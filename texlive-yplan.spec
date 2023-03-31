Name:		texlive-yplan
Version:	34398
Release:	2
Summary:	Daily planner type calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yplan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Prints two six-monthly vertical-type daily planner (i.e.,
months along the top, days downwards), with each 6-month period
fitting onto a single A4 (or US letter) sheet. The package
offers support for English, French, German, Spanish and
Portuguese. The previous scheme of annual updates has now been
abandoned, in favour of a Perl script yplan that generates a
year's planner automatically. (The last manually-generated
LaTeX file remains on the archive.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/yplan
%{_texmfdistdir}/scripts/yplan
%doc %{_texmfdistdir}/doc/latex/yplan

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar texmf-dist/* %{buildroot}%{_texmfdistdir}
