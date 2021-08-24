%define soversion      0.3

Name:           safe-iop
Version:        0.3.1
Release:        1
Summary:        Safe Integer Operations for C

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/redpig/safe-iop
Source :        %{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
Unsafe integer operations are a major cause of software defects even in modern
day software.  C is the underlying language for most high level languages
(Ruby, Python, Java, etc.) in addition to being in widespread general use.
C is a preferred language for high performance programming and is
often used for media file parsing and manipulation. 

Integer overflows occur when the calculated integer requires more storage from
the computing platform than is available.  If a number is too large, not all of
its information can be stored.  This has dangerous side effects. For a detailed
and thorough discussion on integer overflows, please check out CERT's website
on Secure Coding(1) and even Wikipedia(2).

(1) https://www.securecoding.cert.org/confluence/display/seccode/CERT+C+Secure+Coding+Standard
(2) http://en.wikipedia.org/wiki/Integer_overflow

%prep
%autosetup -n %{name}-%{version}/upstream

%build
make so

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/
cp libsafe_iop.so.%{soversion} %{buildroot}%{_libdir}/

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libsafe_iop.so*
