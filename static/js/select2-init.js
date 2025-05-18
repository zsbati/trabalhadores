// Initialize Select2 for all dropdowns
$(document).ready(function() {
    // Initialize all select elements
    $('select.form-select').each(function() {
        var $select = $(this);
        var id = $select.attr('id');
        var placeholder = $select.data('placeholder') || 'Selecione...';
        
        $select.select2({
            theme: 'bootstrap-5',
            width: '100%',
            placeholder: placeholder,
            language: 'pt',
            allowClear: true,
            minimumInputLength: 1
        });
    });
});
