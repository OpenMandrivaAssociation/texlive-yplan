%global tl_name yplan
%global tl_revision 79618
%global tl_bin_links yplan:%{_texmfdistdir}/scripts/yplan/yplan

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Daily planner type calendar
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yplan
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yplan.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(yplan.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Prints two six-monthly vertical-type daily planner (i.e., months along
the top, days downwards), with each 6-month period fitting onto a single
A4 (or US letter) sheet. The package offers support for English, French,
German, Spanish and Portuguese. The previous scheme of annual updates
has now been abandoned, in favour of a Perl script yplan that generates
a year's planner automatically. (The last manually-generated LaTeX file
remains on the archive.)

