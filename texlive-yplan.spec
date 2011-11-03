# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/yplan
# catalog-date 2006-12-16 10:58:44 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-yplan
Version:	20061216
Release:	1
Summary:	Daily planner type calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yplan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Prints two six-monthly vertical-type daily planner (i.e.,
months along the top, days downwards), with each 6-month period
fitting onto a single A4 (or US letter) sheet. The package
offers support for English, French, German, Spanish and
Portuguese. The previous scheme of annual updates has now been
abandoned, in favour of a Perl script yplan that generates a
year's planner automatically. (The last manually-generated
LaTeX file remains on the archive.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/yplan/yplan.sty
%doc %{_texmfdistdir}/doc/latex/yplan/yplan
%doc %{_texmfdistdir}/doc/latex/yplan/yplan.doc
%doc %{_texmfdistdir}/doc/latex/yplan/yplan00.doc
%doc %{_texmfdistdir}/doc/latex/yplan/yplan00a.tex
%doc %{_texmfdistdir}/doc/latex/yplan/yplan00b.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
