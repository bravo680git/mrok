# docker / docker compose: container, image, network, volume and context names, compose
# services. Subcommands and options come from the Fig specs (specs/docker.spec,
# specs/docker-compose.spec); this plugin only fills in the names.
mrok_register __mrok_p_docker docker
mrok_register __mrok_p_compose docker-compose

# Print "name<TAB>description" for one kind of object.
__mrok_docker_list() {
  local f='{{.Names}}	{{.Status}} · {{.Image}}'
  case $1 in
    running) docker ps --format "$f" ;;
    stopped) docker ps -a --filter status=exited --filter status=created --format "$f" ;;
    paused)  docker ps --filter status=paused --format "$f" ;;
    all)     docker ps -a --format "$f" ;;
    image)   docker images --format '{{.Repository}}:{{.Tag}}	{{.Size}} · {{.CreatedSince}}' | grep -v '^<none>' ;;
    network) docker network ls --format '{{.Name}}	{{.Driver}}' ;;
    volume)  docker volume ls --format '{{.Name}}	{{.Driver}}' ;;
    context) docker context ls --format '{{.Name}}	{{.Description}}' ;;
  esac 2>/dev/null
}

# REPLY = what to list at subcommand path $1, argument $2 (0 = value of option $3).
__mrok_docker_kind() {
  local p=${1#container } a=$2
  REPLY=''
  if [ "$a" = 0 ]; then
    case $3 in
      --network|--net) REPLY=network ;;
      --volumes-from) REPLY=all ;;
      --context|-c) REPLY=context ;;
    esac
    return 0
  fi
  case $p in
    exec|attach|top|port)               [ "$a" = 1 ] && REPLY=running ;;
    kill|stop|stats|pause)              REPLY=running ;;
    start)                              REPLY=stopped ;;
    unpause)                            REPLY=paused ;;
    restart|rm|wait|update|inspect)     REPLY=all ;;
    logs|diff|export|commit|rename|cp)  [ "$a" = 1 ] && REPLY=all ;;
    run|create|history|push|tag|'image history'|'image push'|'image tag')
                                        [ "$a" = 1 ] && REPLY=image ;;
    rmi|save|'image rm'|'image save'|'image inspect')
                                        REPLY=image ;;
    'network rm'|'network inspect')     REPLY=network ;;
    'network connect'|'network disconnect')
      case $a in 1) REPLY=network ;; 2) REPLY=all ;; esac ;;
    'volume rm'|'volume inspect')       REPLY=volume ;;
    'context use'|'context rm'|'context inspect'|'context export'|'context update')
                                        [ "$a" = 1 ] && REPLY=context ;;
  esac
  return 0
}

__mrok_p_docker() {
  shift
  if [ "${1-}" = compose ]; then
    shift
    __mrok_compose 1 "$@"
    return
  fi
  case $MROK_CUR in -*) __mrok_spec docker "$@"; return ;; esac
  __mrok_spec_where docker "$@" || return 1
  __mrok_docker_kind "$MROK_PATH" "$MROK_ARG" "$MROK_OPT"
  if [ -n "$REPLY" ]; then
    __mrok_docker_list "$REPLY"
    return 0
  fi
  __mrok_spec docker "$@"
}

__mrok_p_compose() {
  shift
  __mrok_compose 0 "$@"
}

# $1 = 1 for `docker compose`, 0 for `docker-compose`; then the words after it.
# Services come from the compose file in the current directory.
__mrok_compose() {
  local plugin=$1
  shift
  case $MROK_CUR in -*) __mrok_spec docker-compose "$@"; return ;; esac
  __mrok_spec_where docker-compose "$@" || return 1
  local list=0
  case $MROK_PATH in
    exec|run|port|cp) [ "$MROK_ARG" = 1 ] && list=1 ;;
    up|logs|restart|stop|start|kill|pause|unpause|rm|build|pull|push|ps|top|create|images|events)
      [ "$MROK_ARG" -ge 1 ] && list=1 ;;
  esac
  if [ "$list" = 1 ]; then
    # either form works when only one of them is installed
    if [ "$plugin" = 1 ]; then
      docker compose config --services 2>/dev/null || docker-compose config --services 2>/dev/null
    else
      docker-compose config --services 2>/dev/null || docker compose config --services 2>/dev/null
    fi | sed 's/$/	service/' 
    return 0
  fi
  __mrok_spec docker-compose "$@"
}
