%global tl_name fduthesis
%global tl_revision 67231

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9a
Release:	%{tl_revision}.1
Summary:	LaTeX thesis template for Fudan University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fduthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a LaTeX thesis template package for Fudan University. It
can make it easy to write theses both in Chinese and English.

