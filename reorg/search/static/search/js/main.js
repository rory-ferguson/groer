var countries = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.whitespace,
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: 'http://127.0.0.1:8000/autocomplete/',
});
    
countries.initialize();
$('#prefetch .twitter-typeahead').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
}, {
    name: 'countries',
    source: countries
});