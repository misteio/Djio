CKEDITOR.plugins.add('parameterdropdown',
{
    requires: ['richcombo'],
    init: function (editor) {
        //  array of strings to choose from that'll be inserted into the editor
        var strings = [];
        strings.push(['<div class="style-msg successmsg"> <div class="sb-msg"><i class="icon-thumbs-up"></i><strong>Well done!</strong> You successfully read this important alert message.</div> <button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button> </div>', 'Alert Success', 'Alert Success']);
        strings.push(['[FullName]', 'Full Name', 'Full Name']);
        strings.push(['[Email]', 'User Email', 'User Email']);
        strings.push(['[Website]', 'Website', 'Website']);

        // add the menu to the editor
        editor.ui.addRichCombo('parameterdropdown',
        {
            label: 'Alerts',
            title: 'Select Parameter',
            voiceLabel: 'Select Parameter',
            className: 'cke_format',
            multiSelect: false,
            panel:
            {
                css: [editor.config.contentsCss, CKEDITOR.skin.getPath('editor')],
                voiceLabel: editor.lang.panelVoiceLabel
            },

            init: function () {
                this.startGroup("Parameters");
                for (var i in strings) {
                    this.add(strings[i][0], strings[i][1], strings[i][2]);
                }
            },

            onClick: function (value) {
                editor.focus();
                editor.fire('saveSnapshot');
                editor.insertHtml(value);
                editor.fire('saveSnapshot');
            }
        });
    }
});