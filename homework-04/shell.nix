# shell.nix

{ pkgs ? import <nixpkgs> {} }:
let pythonPackages = with pkgs.python311Packages; [
  numpy
  matplotlib
  pandas
  ipython
  scipy
  ];
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    bashInteractive

  ] ++ pythonPackages;
  # Set PKG_CONFIG_PATH to include SDL2.pc
  shellHook = ''
  LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib";
  python -m venv .venv
  source .venv/bin/activate
  .venv/bin/pip3 install notebook
  .venv/bin/jupyter-notebook
  

  '';
}
