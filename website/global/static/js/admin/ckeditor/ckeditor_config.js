CKEDITOR.editorConfig = function( config ) {
	config.toolbar = [
    { name: 'document', items: [ 'Source', '-', 'NewPage', 'Preview', '-', 'Templates' ] },
    '/',
	{ name: 'clipboard', items: [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
		{ name: 'links', items: [ 'Link', 'Unlink', 'Anchor' ] },
		{ name: 'insert', items: [ 'Image', 'Table', 'HorizontalRule', 'SpecialChar' ] },
		{ name: 'tools', items: [ 'Maximize' ] },
		{ name: 'document', items: [ 'Source' ] },
		{ name: 'pageinsertion', items:['pageinsertion'] },

		{ name: 'alignment', items : [ 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock' ] },

		'/',
		{ name: 'basicstyles', items: [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat', 'Embed' ] },
		{ name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CodeSnippet' ] },
		{ name: 'styles', items: [ 'Styles', 'Format' ] },


	];

	config.stylesSet = 'my_styles';
	config.allowedContent = true;
	config.templates_files=['/admin/static/js/ckeditor/ckeditor_template.js'];
	config.templates='site';
	config.language = 'fr';
	config.imageBrowser_listUrl = "/admin/static/images_list.json";
	config.protectedSource.push(/<i[^>]*><\/i>/g);
	config.codeSnippet_theme = 'monokai_sublime';
	config.extraAllowedContent = 'span(*)';
	config.filebrowserBrowseUrl = 'http://172.104.181.128/filemanager/dialog.php?type=1&editor=ckeditor&fldr=&akey=myPrivateKey7777777&crossdomain=1&popup=1&relative_url=1',
	config.filebrowserUploadUrl = 'http://172.104.181.128/filemanager/dialog.php?type=1&editor=ckeditor&fldr=&akey=myPrivateKey7777777&crossdomain=1&popup=1&relative_url=1',
	config.filebrowserImageBrowseUrl = 'http://172.104.181.128/filemanager/dialog.php?type=1&editor=ckeditor&fldr=&akey=myPrivateKey7777777&crossdomain=1&popup=1&relative_url=1'

};

CKEDITOR.stylesSet.add( 'my_styles', [
    // Block-level styles.
    { name: 'Couleur', element: 'span' },

    // Inline styles.
    { name: 'Bleu', element: 'span', attributes: { 'class': 'label label-primary' } },
    { name: 'Vert', element: 'span', attributes: { 'class': 'label label-success' } },
    { name: 'Rouge', element: 'span', attributes: { 'class': 'label label-danger' } },
    { name: 'Jaune', element: 'span', attributes: { 'class': 'label label-warning' } },

]);



