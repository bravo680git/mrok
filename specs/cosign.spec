@	
s	attach	Provides utilities for attaching artifacts to other artifacts in a registry
s	attest	Attest the supplied container image
s	clean	Remove all signatures from an image
s	completion	Generate completion script
s	copy	Copy the supplied container image and signatures
s	dockerfile	Provides utilities for discovering images in and performing operations on Dockerfiles
s	download	Provides utilities for downloading artifacts and attached artifacts in a registry
s	generate	Generates (unsigned) signature payloads from the supplied container image
s	generate-key-pair	Generates a key-pair
s	import-key-pair	Imports a PEM-encoded RSA or EC private key
s	initialize	Initializes SigStore root to retrieve trusted certificate and key targets for verification
s	load	Load a signed image on disk to a remote registry
s	login	Log in to a registry
s	manifest	Provides utilities for discovering images in and performing operations on Kubernetes manifests
s	piv-tool	This cosign was not built with piv-tool support!
s	pkcs11-tool	This cosign was not built with pkcs11-tool support!
s	policy	Subcommand to manage a keyless policy
s	public-key	Gets a public key from the key-pair
s	save	Save the container image and associated signatures to disk at the specified directory
s	sign	Sign the supplied container image
s	sign-blob	Sign the supplied blob, outputting the base64-encoded signature to stdout
s	tree	Display supply chain security related artifacts for an image such as signatures, SBOMs and…
s	triangulate	Outputs the located cosign image reference. This is the location cosign stores the specified…
s	upload	Provides utilities for uploading artifacts to a registry
s	verify	Verify a signature on the supplied container image
s	verify-attestation	Verify an attestation on the supplied container image
s	verify-blob	Verify a signature on the supplied blob
s	version	Prints the version
s	help	Help about any command
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for cosign	
@	attach
s	attestation	Attach attestation to the supplied container image
s	sbom	Attach sbom to the supplied container image
s	signature	Attach signatures to the supplied container image
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for attach	
@	attach attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--attestation	Path to the attestation envelope	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for attestation	
@	attach sbom
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--sbom	Path to the sbom, or {-} for stdin	v
o	--type	Type of sbom (spdx|cyclonedx|syft)	v
o	--help|-h	Help for sbom	
@	attach signature
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--payload	Path to the payload covered by the signature (if using another format)	v
o	--signature	The signature, path to the signature, or {-} for stdin	v
o	--help|-h	Help for signature	
@	attest
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the x509 certificate to include in the Signature	v
o	--force|-f	Skip warnings and confirmations	
o	--fulcio-url	[EXPERIMENTAL] address of sigstore PKI server	v
o	--identity-token	[EXPERIMENTAL] identity token to use for certificate from fulcio	v
o	--insecure-skip-verify	[EXPERIMENTAL] skip verifying fulcio published to the SCT (this should only be used for testing)	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the private key file, KMS URI or Kubernetes Secret	v
o	--no-upload	Do not upload the generated attestation	
o	--oidc-client-id	[EXPERIMENTAL] OIDC client ID for application	v
o	--oidc-client-secret	[EXPERIMENTAL] OIDC client secret for application	v
o	--oidc-issuer	[EXPERIMENTAL] OIDC provider to be used to issue ID token	v
o	--predicate	Path to the predicate file	v
o	--recursive|-r	If a multi-arch image is specified, additionally sign each discrete image	
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--replace		
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--type	Specify a predicate type (slsaprovenance|link|spdx|vuln|custom) or an URI	v
o	--help|-h	Help for attest	
@	clean
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--force|-f	Do not prompt for confirmation	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--type	A type of clean: <signature|attestation|sbom|all> (default: all)	v
o	--help|-h	Help for clean	
@	completion
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for completion	
@	copy
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--force|-f	Overwrite destination image(s), if necessary	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--sig-only	Only copy the image signature	
o	--help|-h	Help for copy	
@	dockerfile
s	verify	Verify a signature on the base image specified in the Dockerfile
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for dockerfile	
@	dockerfile verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--base-image-only	Only verify the base image (the last FROM image in the Dockerfile)	
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--signature-digest-algorithm	Digest algorithm to use when processing a signature (sha224|sha256|sha384|sha512)	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify	
@	download
s	attestation	Download in-toto attestations from the supplied container image
s	sbom	Download SBOMs from the supplied container image
s	signature	Download signatures from the supplied container image
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for download	
@	download attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for attestation	
@	download sbom
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for sbom	
@	download signature
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for signature	
@	generate
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for generate	
@	generate-key-pair
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--kms	Create key pair in KMS service to use for signing	v
o	--help|-h	Help for generate-key-pair	
@	import-key-pair
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--key	Import key pair to use for signing	v
o	--help|-h	Help for import-key-pair	
@	initialize
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--mirror	GCS bucket to a SigStore TUF repository or HTTP(S) base URL	v
o	--root	Path to trusted initial root. defaults to embedded root	v
o	--help|-h	Help for initialize	
@	load
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--dir	Path to directory where the signed image is stored on disk	v
o	--help|-h	Help for load	
@	login
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--password|-p	Password	v
o	--password-stdin	Take the password from stdin	
o	--username|-u	Username	v
o	--help|-h	Help for login	
@	manifest
s	verify	Verify all signatures of images specified in the manifest
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for manifest	
@	manifest verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--signature-digest-algorithm	Digest algorithm to use when processing a signature (sha224|sha256|sha384|sha512)	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify	
@	piv-tool
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for piv-tool	
@	pkcs11-tool
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for pkcs11-tool	
@	policy
s	init	Generate a new keyless policy
s	sign	Sign a keyless policy
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for policy	
@	policy init
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--expires	Total expire duration in days	v
o	--issuer	Trusted issuer to use for identity tokens, e.g. https://accounts.google.com	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--maintainers|-m	List of maintainers to add to the root policy	v
o	--namespace	Registry namespace that the root policy belongs to	v
o	--out	Output policy locally	v
o	--threshold	Threshold for root policy signers	v
o	--help|-h	Help for init	
@	policy sign
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--fulcio-url	[EXPERIMENTAL] address of sigstore PKI server	v
o	--identity-token	[EXPERIMENTAL] identity token to use for certificate from fulcio	v
o	--insecure-skip-verify	[EXPERIMENTAL] skip verifying fulcio published to the SCT (this should only be used for testing)	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--namespace	Registry namespace that the root policy belongs to	v
o	--oidc-client-id	[EXPERIMENTAL] OIDC client ID for application	v
o	--oidc-client-secret	[EXPERIMENTAL] OIDC client secret for application	v
o	--oidc-issuer	[EXPERIMENTAL] OIDC provider to be used to issue ID token	v
o	--out	Output policy locally	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--help|-h	Help for sign	
@	public-key
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--key	Path to the private key file, KMS URI or Kubernetes Secret	v
o	--outfile	Path to a payload file to use rather than generating one	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for public-key	
@	save
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--dir	Path to dir where the signed image should be stored on disk	v
o	--help|-h	Help for save	
@	sign
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the x509 certificate to include in the Signature	v
o	--force|-f	Skip warnings and confirmations	
o	--fulcio-url	[EXPERIMENTAL] address of sigstore PKI server	v
o	--identity-token	[EXPERIMENTAL] identity token to use for certificate from fulcio	v
o	--insecure-skip-verify	[EXPERIMENTAL] skip verifying fulcio published to the SCT (this should only be used for testing)	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the private key file, KMS URI or Kubernetes Secret	v
o	--oidc-client-id	[EXPERIMENTAL] OIDC client ID for application	v
o	--oidc-client-secret	[EXPERIMENTAL] OIDC client secret for application	v
o	--oidc-issuer	[EXPERIMENTAL] OIDC provider to be used to issue ID token	v
o	--output-certificate	Write the certificate to FILE	v
o	--output-signature	Write the signature to FILE	v
o	--payload	Path to a payload file to use rather than generating one	v
o	--recursive|-r	If a multi-arch image is specified, additionally sign each discrete image	
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--upload	Whether to upload the signature	
o	--help|-h	Help for sign	
@	sign-blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--b64	Whether to base64 encode the output	
o	--bundle	Write everything required to verify the blob to a FILE	v
o	--fulcio-url	[EXPERIMENTAL] address of sigstore PKI server	v
o	--identity-token	[EXPERIMENTAL] identity token to use for certificate from fulcio	v
o	--insecure-skip-verify	[EXPERIMENTAL] skip verifying fulcio published to the SCT (this should only be used for testing)	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the private key file, KMS URI or Kubernetes Secret	v
o	--oidc-client-id	[EXPERIMENTAL] OIDC client ID for application	v
o	--oidc-client-secret	[EXPERIMENTAL] OIDC client secret for application	v
o	--oidc-issuer	[EXPERIMENTAL] OIDC provider to be used to issue ID token	v
o	--output	Write the signature to FILE	v
o	--output-certificate	Write the certificate to FILE	v
o	--output-signature	Write the signature to FILE	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for sign-blob	
@	tree
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for tree	
@	triangulate
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--type	Related attachment to triangulate (attestation|sbom|signature), default signature	v
o	--help|-h	Help for triangulate	
@	upload
s	blob	Upload one or more blobs to the supplied container image address
s	wasm	Upload a wasm module to the supplied container image reference
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for upload	
@	upload blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--ct	Content type to set	v
o	--files|-f	<filepath>:[platform/arch]	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for blob	
@	upload wasm
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--file|-f	Path to the wasm file to upload	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for wasm	
@	verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--signature-digest-algorithm	Digest algorithm to use when processing a signature (sha224|sha256|sha384|sha512)	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify	
@	verify-attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--policy	Specify CUE or Rego files will be using for validation	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--type	Specify a predicate type (slsaprovenance|link|spdx|vuln|custom) or an URI	v
o	--help|-h	Help for verify-attestation	
@	verify-blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--bundle	Path to bundle FILE	v
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify-blob	
@	version
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--json	Print JSON instead of text	
o	--help|-h	Help for version	
@	help
s	attach	Provides utilities for attaching artifacts to other artifacts in a registry
s	attest	Attest the supplied container image
s	clean	Remove all signatures from an image
s	completion	Generate completion script
s	copy	Copy the supplied container image and signatures
s	dockerfile	Provides utilities for discovering images in and performing operations on Dockerfiles
s	download	Provides utilities for downloading artifacts and attached artifacts in a registry
s	generate	Generates (unsigned) signature payloads from the supplied container image
s	generate-key-pair	Generates a key-pair
s	import-key-pair	Imports a PEM-encoded RSA or EC private key
s	initialize	Initializes SigStore root to retrieve trusted certificate and key targets for verification
s	load	Load a signed image on disk to a remote registry
s	login	Log in to a registry
s	manifest	Provides utilities for discovering images in and performing operations on Kubernetes manifests
s	piv-tool	This cosign was not built with piv-tool support!
s	pkcs11-tool	This cosign was not built with pkcs11-tool support!
s	policy	Subcommand to manage a keyless policy
s	public-key	Gets a public key from the key-pair
s	save	Save the container image and associated signatures to disk at the specified directory
s	sign	Sign the supplied container image
s	sign-blob	Sign the supplied blob, outputting the base64-encoded signature to stdout
s	tree	Display supply chain security related artifacts for an image such as signatures, SBOMs and…
s	triangulate	Outputs the located cosign image reference. This is the location cosign stores the specified…
s	upload	Provides utilities for uploading artifacts to a registry
s	verify	Verify a signature on the supplied container image
s	verify-attestation	Verify an attestation on the supplied container image
s	verify-blob	Verify a signature on the supplied blob
s	version	Prints the version
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for help	
@	help attach
s	attestation	Attach attestation to the supplied container image
s	sbom	Attach sbom to the supplied container image
s	signature	Attach signatures to the supplied container image
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help attach attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--attestation	Path to the attestation envelope	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for attestation	
@	help attach sbom
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--sbom	Path to the sbom, or {-} for stdin	v
o	--type	Type of sbom (spdx|cyclonedx|syft)	v
o	--help|-h	Help for sbom	
@	help attach signature
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--payload	Path to the payload covered by the signature (if using another format)	v
o	--signature	The signature, path to the signature, or {-} for stdin	v
o	--help|-h	Help for signature	
@	help attest
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help clean
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help completion
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help copy
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help dockerfile
s	verify	Verify a signature on the base image specified in the Dockerfile
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help dockerfile verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--base-image-only	Only verify the base image (the last FROM image in the Dockerfile)	
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--signature-digest-algorithm	Digest algorithm to use when processing a signature (sha224|sha256|sha384|sha512)	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify	
@	help download
s	attestation	Download in-toto attestations from the supplied container image
s	sbom	Download SBOMs from the supplied container image
s	signature	Download signatures from the supplied container image
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help download attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for attestation	
@	help download sbom
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for sbom	
@	help download signature
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for signature	
@	help generate
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help generate-key-pair
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help import-key-pair
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help initialize
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help load
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help login
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help manifest
s	verify	Verify all signatures of images specified in the manifest
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help manifest verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--annotations|-a	Extra key=value pairs to sign	v
o	--attachment	Related image attachment to sign (sbom), default none	v
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--cert	Path to the public certificate	v
o	--cert-email	The email expected in a valid Fulcio certificate	v
o	--cert-oidc-issuer	The OIDC issuer expected in a valid Fulcio certificate, e.g. https://token.actions.githubuserconten…	v
o	--check-claims	Whether to check the claims found	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--key	Path to the public key file, KMS URI or Kubernetes Secret	v
o	--local-image	Whether the specified image is a path to an image saved locally via 'cosign save'	
o	--output|-o	Output format for the signing image information (json|text)	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--signature	Signature content or path or remote URL	v
o	--signature-digest-algorithm	Digest algorithm to use when processing a signature (sha224|sha256|sha384|sha512)	v
o	--sk	Whether to use a hardware security key	
o	--slot	Security key slot to use for generated key (default: signature)…	v
o	--help|-h	Help for verify	
@	help piv-tool
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help pkcs11-tool
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help policy
s	init	Generate a new keyless policy
s	sign	Sign a keyless policy
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help policy init
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--expires	Total expire duration in days	v
o	--issuer	Trusted issuer to use for identity tokens, e.g. https://accounts.google.com	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--maintainers|-m	List of maintainers to add to the root policy	v
o	--namespace	Registry namespace that the root policy belongs to	v
o	--out	Output policy locally	v
o	--threshold	Threshold for root policy signers	v
o	--help|-h	Help for init	
@	help policy sign
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--fulcio-url	[EXPERIMENTAL] address of sigstore PKI server	v
o	--identity-token	[EXPERIMENTAL] identity token to use for certificate from fulcio	v
o	--insecure-skip-verify	[EXPERIMENTAL] skip verifying fulcio published to the SCT (this should only be used for testing)	
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--namespace	Registry namespace that the root policy belongs to	v
o	--oidc-client-id	[EXPERIMENTAL] OIDC client ID for application	v
o	--oidc-client-secret	[EXPERIMENTAL] OIDC client secret for application	v
o	--oidc-issuer	[EXPERIMENTAL] OIDC provider to be used to issue ID token	v
o	--out	Output policy locally	v
o	--rekor-url	[EXPERIMENTAL] address of rekor STL server	v
o	--help|-h	Help for sign	
@	help public-key
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help save
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help sign
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help sign-blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help tree
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help triangulate
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help upload
s	blob	Upload one or more blobs to the supplied container image address
s	wasm	Upload a wasm module to the supplied container image reference
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help upload blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--ct	Content type to set	v
o	--files|-f	<filepath>:[platform/arch]	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for blob	
@	help upload wasm
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--allow-insecure-registry	Whether to allow insecure connections to registries. Don't use this for anything but testing	
o	--attachment-tag-prefix	Optional custom prefix to use for attached image tags. Attachment images are tagged as…	v
o	--file|-f	Path to the wasm file to upload	v
o	--k8s-keychain	Whether to use the kubernetes keychain instead of the default keychain (supports workload identity)	
o	--help|-h	Help for wasm	
@	help verify
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help verify-attestation
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help verify-blob
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
@	help version
o	--output-file	Log output to a file	v
o	--timeout|-t	Timeout for commands	v
o	--verbose|-d	Log debug output	
o	--help|-h	Help for version	
