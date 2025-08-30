{
  description = "pynumber dev environment (ruff, pyright, uv)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      lib = nixpkgs.lib;
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forAllSystems =
        f:
        builtins.listToAttrs (
          map (system: {
            name = system;
            value = f system;
          }) systems
        );
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python311
              uv
              ruff
              pyright
            ];
            # Enable running manylinux-style dynamically linked executables (e.g., uv-build) on NixOS
            shellHook = ''
              # Prefix prompt to show we are inside the flake dev shell (resilient to .bashrc)
              export NIX_SHELL_PROMPT_PREFIX="(pynumber-dev) "
              if [ -n "$PS1" ]; then
                # Prefix immediately for current prompt
                case "$PS1" in
                  *"(pynumber-dev)"*) ;;
                  *) PS1="''${NIX_SHELL_PROMPT_PREFIX}$PS1" ;;
                esac
                __pynumber_prompt_prefix() {
                  case "$PS1" in
                    *"(pynumber-dev)"*) ;;
                    *) PS1="''${NIX_SHELL_PROMPT_PREFIX}$PS1" ;;
                  esac
                }
                case "$PROMPT_COMMAND" in
                  *"__pynumber_prompt_prefix"*) ;;
                  *) export PROMPT_COMMAND="__pynumber_prompt_prefix''${PROMPT_COMMAND:+; }$PROMPT_COMMAND" ;;
                esac
              fi
              if [ -e /etc/os-release ] && grep -qi '^ID=nixos' /etc/os-release; then
                export NIX_LD="${pkgs.stdenv.cc.bintools.dynamicLinker}"
                export NIX_LD_LIBRARY_PATH="${
                  lib.makeLibraryPath [
                    pkgs.glibc
                    pkgs.zlib
                    pkgs.openssl
                    pkgs.libffi
                    pkgs.stdenv.cc.cc
                  ]
                }"
                echo "nix-ld env set for running dynamically linked binaries"
              fi
              echo "Dev shell ready: python=$(python --version), ruff=$(ruff --version | head -n1), pyright=$(pyright --version)"
              echo "Run: make setup && make lint && make test; to build: uv build"
            '';
          };
        }
      );
    };
}
