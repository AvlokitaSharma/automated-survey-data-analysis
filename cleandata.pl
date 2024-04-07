#!/usr/bin/perl
use strict;
use warnings;
use Text::CSV;

my $csv = Text::CSV->new({ binary => 1, eol => "\n" });
open my $in, '<', 'survey_responses.csv' or die "Cannot open input file: $!";
open my $out, '>', 'cleaned_responses.csv' or die "Cannot open output file: $!";

while (my $row = $csv->getline($in)) {
    for (@$row) {
        s/^\s+|\s+$//g; 
        $_ = lc($_); 
    }
    $csv->print($out, $row);
}

close $in;
close $out;
