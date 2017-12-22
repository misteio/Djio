CKEDITOR.editorConfig = function( config ) {
	config.toolbar = [
		{ name: 'clipboard', items: [ 'Undo', 'Redo', '-', 'Link', 'Unlink', '-', 'Bold', 'Italic', 'Underline', 'Strike', '-','Format','Styles', 'RemoveFormat' ] },
	];

	config.stylesSet = 'my_styles';

};

CKEDITOR.dtd.$editable.span = 1
CKEDITOR.dtd.$editable.a = 1

CKEDITOR.stylesSet.add( 'my_styles', [
    // Inline styles.
    { name: 'Blue', element: 'span', attributes: { 'class': 'label label-primary' } },
    { name: 'Green', element: 'span', attributes: { 'class': 'label label-success' } },
    { name: 'Red', element: 'span', attributes: { 'class': 'label label-danger' } },
    { name: 'Yellow', element: 'span', attributes: { 'class': 'label label-warning' } },
]);



