CKEDITOR.editorConfig = function( config ) {
	config.toolbar = [
		{ name: 'document', items: [ 'Source', '-', 'NewPage', 'Preview', '-', 'Templates' ] },
		{ name: 'clipboard', items: [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
		{ name: 'links', items: [ 'Link', 'Unlink', 'Anchor' ] },
		{ name: 'tools', items: [ 'Maximize' ] },
		'/',
		{ name: 'basicstyles', items: [ 'Bold', 'Italic', 'Underline', 'Strike', '-', 'Image', 'Embed' ] },
		{ name: 'alignment', items : [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock' ] },
		{ name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'Table', 'HorizontalRule' ] },
		'/',
		{ name: 'pageinsertion', items:['pageinsertion', 'Format','Styles', 'RemoveFormat'] },
	];

	config.stylesSet = 'my_styles';
	config.allowedContent = true;
	config.templates_files=['/static/js/admin/ckeditor/ckeditor_template.js'];
	config.templates='site';
	config.protectedSource.push(/<i[^>]*><\/i>/g);
	config.extraAllowedContent = 'span(*)';
	config.filebrowserBrowseUrl= '/admin/roxyfileman/';
	config.filebrowserUploadUrl = '/admin/ckeditor-upload';

};

CKEDITOR.stylesSet.add( 'my_styles', [
    // Inline styles.
    { name: 'Blue', element: 'span', attributes: { 'class': 'label label-primary' } },
    { name: 'Green', element: 'span', attributes: { 'class': 'label label-success' } },
    { name: 'Red', element: 'span', attributes: { 'class': 'label label-danger' } },
    { name: 'Yellow', element: 'span', attributes: { 'class': 'label label-warning' } },

]);



