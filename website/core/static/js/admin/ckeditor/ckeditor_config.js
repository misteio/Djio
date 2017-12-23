CKEDITOR.editorConfig = function( config ) {
	config.toolbar = [
		{ name: 'clipboard', items: [ 'Undo', 'Redo', '-', 'Link', 'Unlink', '-', 'Bold', 'Italic', 'Underline', 'Strike', '-','Format','Styles', 'RemoveFormat' ] },
	];

	config.stylesSet = 'my_styles';
};


CKEDITOR.stylesSet.add( 'my_styles', [
    { name: 'Basic Color', element: 'span', attributes: { 'class': 'basic-color' } },
    { name: 'Blue', element: 'span', attributes: { 'class': 'label label-primary' } },
    { name: 'Green', element: 'span', attributes: { 'class': 'label label-success' } },
    { name: 'Red', element: 'span', attributes: { 'class': 'label label-danger' } },
    { name: 'Yellow', element: 'span', attributes: { 'class': 'label label-warning' } },
    { name: 'List', element: 'span', attributes: { 'class': 'list-dots' } },
]);



