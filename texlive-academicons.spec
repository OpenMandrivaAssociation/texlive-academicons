Name:		texlive-academicons
Version:	62622
Release:	1
Summary:	Font containing high quality icons of online academic profiles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/academicons
License:	lppl1.3c ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/academicons.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/academicons.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The academicons package provides access in (La)TeX to 124 high
quality icons of online academic profiles included in the free
"Academicons" font. This package requires either the Xe(La)TeX
or Lua(La)TeX engine to load the "Academicons" font from the
system, which requires installing the bundled academicons.ttf
font file. As new releases come out, it is recommended to
install the bundled font version as there may be differences
between the package and previous font versions or newest font
versions not yet contemplated in the package. The "Academicons"
font was designed by James Walsh and released (see
http://jpswalsh.github.io/academicons/) under the open SIL Open
Font License. This package is a redistribution of the free
"Academicons" font with specific bindings for (La)TeX. It is
inspired and based on the fontawesome package. The academicons
package provides the generic \aiicon command to access icons,
which takes as mandatory argument the name of the desired icon.
It also provides individual direct commands for each specific
icon. The full list of icons and their respective names and
direct commands can be found in the manual. For example,
\aiicon{googlescholar} yields the same result as
\aiGoogleScholar.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/academicons
%{_texmfdistdir}/fonts/truetype/public/academicons
%doc %{_texmfdistdir}/doc/fonts/academicons

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
