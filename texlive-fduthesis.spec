Name:		texlive-fduthesis
Version:	64288
Release:	1
Summary:	LaTeX thesis template for Fudan University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fduthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fduthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a LaTeX thesis template package for Fudan
University. It can make it easy to write theses both in Chinese
and English.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fduthesis
%{_texmfdistdir}/tex/latex/fduthesis
%doc %{_texmfdistdir}/doc/latex/fduthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
