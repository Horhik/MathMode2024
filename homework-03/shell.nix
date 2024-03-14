# shell.nix

{ pkgs ? import <nixpkgs> {} }:
let pythonPackages = with pkgs.python311Packages; [
  flask
  requests
  ];
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    SDL2
    raylib
    bashInteractive
    pkg-config
    glfw
    SDL2  # SDL2 library


  ] ++ pythonPackages;
  # Set PKG_CONFIG_PATH to include SDL2.pc
  shellHook = ''
    export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:${pkgs.SDL2.dev}/lib/pkgconfig
    export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:${pkgs.pkg-config}
    export LD_LIBRARY_PATH=${pkgs.SDL2}/lib
    export raylib_DIR=${pkgs.raylib}/lib/cmake/raylib/
    export raylib_LIBRARY=${pkgs.raylib}/lib
    export raylib_INCLUDE_DIR=${pkgs.raylib}/include


  '';
}
