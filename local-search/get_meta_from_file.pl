#!/usr/bin/perl

use strict;
use warnings;
use 5.016;
use Image::ExifTool;
use Cwd;
use experimental 'smartmatch';

my $dir = shift @ARGV;
#if directory not specified, current directory will be used
unless (defined $dir) {$dir=cwd;}
my @valid_formats = qw(WAV OPUS);
my @valid_files_array;
my $tag = "FileType";

#Create object
my $exifTool = new Image::ExifTool;

my @files_in_dir = qx/ls $dir/;
chomp(@files_in_dir);

foreach (@files_in_dir) {
		my $success = $exifTool->ExtractInfo($dir.$_);
		next unless $success; 	#stands for unless($success) {next}
		my $val = $exifTool->GetValue($tag);
		if ($val ~~ @valid_formats) { push @valid_files_array, $_ };
	}
$"="%";
print "@valid_files_array";
