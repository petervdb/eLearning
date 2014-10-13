#!/usr/bin/perl -w
use MongoDB;
use MongoDB::OID;

my $db = $client->get_database( 'tutorial' );
$db->get_collection( 'perl_test' )->insert( { a => 1, b => 1 } );
