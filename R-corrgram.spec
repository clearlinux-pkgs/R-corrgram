#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-corrgram
Version  : 1.13
Release  : 1
URL      : https://cran.r-project.org/src/contrib/corrgram_1.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/corrgram_1.13.tar.gz
Summary  : Plot a Correlogram
Group    : Development/Tools
License  : GPL-3.0
Requires: R-bitops
Requires: R-seriation
BuildRequires : R-bitops
BuildRequires : R-seriation
BuildRequires : buildreq-R

%description
graphically. Included panel functions can display points, shading, ellipses, and

%prep
%setup -q -c -n corrgram

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552835733

%install
export SOURCE_DATE_EPOCH=1552835733
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrgram
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrgram
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrgram
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  corrgram || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/corrgram/DESCRIPTION
/usr/lib64/R/library/corrgram/INDEX
/usr/lib64/R/library/corrgram/Meta/Rd.rds
/usr/lib64/R/library/corrgram/Meta/data.rds
/usr/lib64/R/library/corrgram/Meta/features.rds
/usr/lib64/R/library/corrgram/Meta/hsearch.rds
/usr/lib64/R/library/corrgram/Meta/links.rds
/usr/lib64/R/library/corrgram/Meta/nsInfo.rds
/usr/lib64/R/library/corrgram/Meta/package.rds
/usr/lib64/R/library/corrgram/Meta/vignette.rds
/usr/lib64/R/library/corrgram/NAMESPACE
/usr/lib64/R/library/corrgram/R/corrgram
/usr/lib64/R/library/corrgram/R/corrgram.rdb
/usr/lib64/R/library/corrgram/R/corrgram.rdx
/usr/lib64/R/library/corrgram/data/Rdata.rdb
/usr/lib64/R/library/corrgram/data/Rdata.rds
/usr/lib64/R/library/corrgram/data/Rdata.rdx
/usr/lib64/R/library/corrgram/doc/corrgram_cov2cor.R
/usr/lib64/R/library/corrgram/doc/corrgram_cov2cor.Rmd
/usr/lib64/R/library/corrgram/doc/corrgram_cov2cor.html
/usr/lib64/R/library/corrgram/doc/corrgram_examples.R
/usr/lib64/R/library/corrgram/doc/corrgram_examples.Rmd
/usr/lib64/R/library/corrgram/doc/corrgram_examples.html
/usr/lib64/R/library/corrgram/doc/index.html
/usr/lib64/R/library/corrgram/help/AnIndex
/usr/lib64/R/library/corrgram/help/aliases.rds
/usr/lib64/R/library/corrgram/help/corrgram.rdb
/usr/lib64/R/library/corrgram/help/corrgram.rdx
/usr/lib64/R/library/corrgram/help/paths.rds
/usr/lib64/R/library/corrgram/html/00Index.html
/usr/lib64/R/library/corrgram/html/R.css
/usr/lib64/R/library/corrgram/tests/testthat.R
/usr/lib64/R/library/corrgram/tests/testthat/test_bounds.R
/usr/lib64/R/library/corrgram/tests/testthat/test_misc.R
/usr/lib64/R/library/corrgram/tests/testthat/test_order.R
/usr/lib64/R/library/corrgram/tests/testthat/test_outerlabels.R