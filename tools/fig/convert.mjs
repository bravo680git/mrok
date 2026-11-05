// Convert Fig completion specs (github.com/withfig/autocomplete, MIT) into mrok's
// line-based .spec format. Run once by a maintainer; the output is committed.
//
//   git clone --depth 1 https://github.com/withfig/autocomplete fig
//   (cd fig && npm install --ignore-scripts && npx @withfig/autocomplete-tools compile)
//   node tools/fig/convert.mjs fig/build specs
//
// Only top-level specs (build/<cmd>.js) are converted. Commands whose spec is split into
// a folder (aws/, gcloud/, dotnet/, php/, ...) are skipped entirely; a subcommand that
// loads another spec keeps only its name.
// Anything that needs JavaScript at completion time (postProcess, custom generators,
// generateSpec, ...) is dropped and listed in tools/fig/DYNAMIC.md.
//
// Output format (TAB-separated, one record per line):
//   @ <path>              node: <path> = subcommand names after the command ("" = root)
//     s <names> <desc>                subcommand, names joined with "|"
//     o <names> <desc> <flags>        option; flags: v takes a value, V optional value,
//                                     = value goes after "=", p inherited by subcommands
//     a <count> <variadic>            positional arguments of this node
//   = <path> <option>     values for an option's argument
//   # <path> <index>      values for a positional argument (1-based)
//     v <value> <desc>                a suggestion
//     t <templates>                   filepaths/folders: use the shell's completion
//     g <command> <split>             run <command>, one suggestion per piece
//     d                               dynamic in Fig, not converted: use the shell's completion

import {
  readdirSync,
  writeFileSync,
  mkdirSync,
  rmSync,
  existsSync,
  statSync,
} from "node:fs";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const [buildDir, outDir] = process.argv.slice(2).map((p) => p && resolve(p));
if (!buildDir || !outDir) {
  console.error("usage: node convert.mjs <fig/build> <out dir>");
  process.exit(2);
}

// Commands that already have a hand-written mrok plugin.
const SKIP = new Set(["git", "npm", "pnpm", "yarn", "bun", "make"]);
// Shell keywords and command prefixes: mrok looks past these to the real command.
const KEYWORDS = new Set(
  "if for while until then do else elif case select repeat function time nocorrect noglob command exec builtin sudo nohup doas".split(" "),
);

const clean = (s) =>
  String(s ?? "")
    .split("\n")[0]
    .replace(/[\t\r]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
// Descriptions: the popup shows one short line, so cut long ones at a word boundary.
const MAX_DESC = 100;
const desc = (s) => {
  const d = clean(s);
  if (d.length <= MAX_DESC) return d;
  const cut = d.slice(0, MAX_DESC - 1);
  return cut.slice(0, cut.lastIndexOf(" ") > 60 ? cut.lastIndexOf(" ") : cut.length).replace(/[\s,.;:]+$/, "") + "…";
};
const names = (n) =>
  (Array.isArray(n) ? n : [n]).filter(
    (x) => typeof x === "string" && x && !/[\t|\n]/.test(x),
  );
const arr = (x) => (x == null ? [] : Array.isArray(x) ? x : [x]);
const shq = (s) =>
  /^[\w@%+=:,./-]+$/.test(s) ? s : `'${String(s).replace(/'/g, `'\\''`)}'`;

function convert(spec) {
  const out = [];
  const dyn = []; // [path, what]

  // Returns the slot lines for one Fig arg (or [] when there's nothing to say).
  function argLines(arg, where) {
    const lines = [];
    for (const s of arr(arg.suggestions)) {
      if (typeof s === "string") lines.push(`v\t${clean(s)}\t`);
      else if (s && !s.hidden)
        for (const n of names(s.name))
          lines.push(`v\t${clean(n)}\t${desc(s.description)}`);
    }
    const tpl = new Set(arr(arg.template));
    let dynamic = false;
    for (const g of arr(arg.generators)) {
      if (!g) continue;
      for (const t of arr(g.template)) tpl.add(t);
      const fnBits = [
        "postProcess",
        "custom",
        "trigger",
        "getQueryTerm",
      ].filter((k) => typeof g[k] === "function");
      if (typeof g.script === "function") fnBits.push("script()");
      if (g.script && !fnBits.length) {
        const cmd = Array.isArray(g.script)
          ? g.script.map(shq).join(" ")
          : String(g.script);
        const split = g.splitOn ?? "\n";
        if (!/[\t\n]/.test(cmd) && typeof split === "string") {
          lines.push(
            `g\t${cmd}\t${split.replace(/\n/g, "\\n").replace(/\t/g, "\\t")}`,
          );
          continue;
        }
      }
      if (g.script || g.custom || fnBits.length) {
        dynamic = true;
        dyn.push([where, fnBits.length ? fnBits.join("+") : "script"]);
      }
    }
    if (tpl.size) lines.push(`t\t${[...tpl].join(",")}`);
    if (dynamic) lines.push("d");
    return lines;
  }

  function walk(node, path) {
    const head = [`@\t${path}`];
    const slots = [];
    const children = [];
    if (typeof node.generateSpec === "function")
      dyn.push([path || "(root)", "generateSpec"]);
    if (node.additionalSuggestions)
      dyn.push([path || "(root)", "additionalSuggestions"]);

    for (const sc of arr(node.subcommands)) {
      if (!sc || sc.hidden) continue;
      const ns = names(sc.name);
      if (!ns.length) continue;
      head.push(`s\t${ns.join("|")}\t${desc(sc.description)}`);
      if (sc.loadSpec)
        dyn.push([
          `${path} ${ns[0]}`.trim(),
          typeof sc.loadSpec === "function"
            ? "loadSpec()"
            : `loadSpec ${sc.loadSpec}`,
        ]);
      children.push([sc, `${path} ${ns[0]}`.trim()]);
    }
    for (const o of arr(node.options)) {
      if (!o || o.hidden) continue;
      const ns = names(o.name);
      if (!ns.length) continue;
      const args = arr(o.args);
      let flags = "";
      if (args.length) flags += args[0].isOptional ? "V" : "v";
      if (
        o.requiresSeparator === true ||
        o.requiresSeparator === "=" ||
        o.requiresEquals
      )
        flags += "=";
      if (o.isPersistent) flags += "p";
      head.push(`o\t${ns.join("|")}\t${desc(o.description)}\t${flags}`);
      if (args.length) {
        const l = argLines(args[0], `${path} ${ns[0]}`.trim());
        if (l.length) slots.push(`=\t${path}\t${ns[0]}`, ...l);
      }
    }
    const args = arr(node.args);
    if (args.length) {
      head.push(
        `a\t${args.length}\t${args[args.length - 1].isVariadic ? 1 : 0}`,
      );
      args.forEach((a, i) => {
        const l = argLines(a || {}, `${path} <arg${i + 1}>`.trim());
        if (l.length) slots.push(`#\t${path}\t${i + 1}`, ...l);
      });
    }
    out.push(...head, ...slots);
    for (const [sc, p] of children) walk(sc, p);
  }

  walk(spec, "");
  return { text: out.join("\n") + "\n", dyn };
}

const files = readdirSync(buildDir).filter((f) => f.endsWith(".js"));
if (existsSync(outDir))
  for (const f of readdirSync(outDir))
    if (f.endsWith(".spec")) rmSync(join(outDir, f));
mkdirSync(outDir, { recursive: true });

const index = [];
const report = [];
const skipped = [];
for (const f of files.sort()) {
  const cmd = f.slice(0, -3);
  if (SKIP.has(cmd)) {
    skipped.push(`${cmd} (mrok plugin)`);
    continue;
  }
  if (KEYWORDS.has(cmd)) {
    skipped.push(`${cmd} (shell keyword)`);
    continue;
  }
  // Big multi-file specs (aws, gcloud, dotnet, php, ...): not worth shipping.
  if (existsSync(join(buildDir, cmd)) && statSync(join(buildDir, cmd)).isDirectory()) {
    skipped.push(`${cmd} (sub-spec folder)`);
    continue;
  }
  if (!/^[A-Za-z0-9][A-Za-z0-9._+-]*$/.test(cmd)) {
    skipped.push(`${cmd} (name)`);
    continue;
  }
  let spec;
  try {
    spec = (await import(pathToFileURL(join(buildDir, f)).href)).default;
  } catch (e) {
    skipped.push(`${cmd} (load error: ${clean(e.message)})`);
    continue;
  }
  if (!spec || typeof spec !== "object" || Array.isArray(spec)) {
    skipped.push(`${cmd} (not a static spec)`);
    continue;
  }
  const { text, dyn } = convert(spec);
  writeFileSync(join(outDir, `${cmd}.spec`), text);
  index.push(`${cmd}\t${desc(spec.description)}`);
  if (dyn.length) report.push({ cmd, dyn });
}
writeFileSync(join(outDir, "index"), index.join("\n") + "\n");

// Report of what was not converted, for deciding which commands deserve a hand-written plugin.
report.sort(
  (a, b) => b.dyn.length - a.dyn.length || a.cmd.localeCompare(b.cmd),
);
const md = [
  "# Dynamic parts of Fig specs that were not converted",
  "",
  "Generated by `tools/fig/convert.mjs`. These need JavaScript in Fig (postProcess, custom",
  "generators, loadSpec of a sub-spec folder, ...). mrok falls back to the shell's own",
  "completion at these positions. Port the useful ones by hand as plugins in `plugins/`.",
  "",
  `Specs converted: ${index.length}. Skipped: ${skipped.length} (${skipped.join(", ")}).`,
  "",
  "| Command | Count | Where (first 6) |",
  "| --- | ---: | --- |",
  ...report.map(({ cmd, dyn }) => {
    const where = dyn
      .slice(0, 6)
      .map(
        ([p, w]) => `\`${cmd}${p && !p.startsWith("(") ? " " + p : ""}\` ${w}`,
      )
      .join("; ");
    return `| ${cmd} | ${dyn.length} | ${where.replace(/\|/g, "\\|")}${dyn.length > 6 ? " …" : ""} |`;
  }),
  "",
];
writeFileSync(new URL("./DYNAMIC.md", import.meta.url), md.join("\n"));
console.log(
  `converted ${index.length}, skipped ${skipped.length}, with dynamic parts ${report.length}`,
);
