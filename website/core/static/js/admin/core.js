$('.select2').select2()

function activeClickDelete(url, title, message)
{
    iziToast.question({
        timeout: 20000,
        close: false,
        overlay: true,
        toastOnce: true,
        zindex: 999,
        title: 'Hey',
        message: message ? message : gettext('Are you sure to delete <b>') + title + '</>?',
        position: 'center',
        buttons: [
            ['<button><b>' + gettext('Yes') + '</b></button>', function (instance, toast) {
                instance.hide(toast, { transitionOut: 'fadeOut' }, 'button');
                window.location = url;
            }, true],
            ['<button>' + gettext('No') + '</button>', function (instance, toast) {
                instance.hide(toast, { transitionOut: 'fadeOut' }, 'button');
            }]
        ],
    });
}


function fancyTreeInit(fancytree, nodes, renderColumns, url){
    fancytree.fancytree({
            extensions: ["glyph", "table", "wide", "dnd"],
            selectMode: 3,
            glyph: {
                preset: "awesome4",
                map: {}
            },
            table: {
                nodeColumnIdx: 0
            },
            source: nodes,
            renderColumns: renderColumns,
            dnd: {
                autoExpandMS: 400,
                draggable: {
                    zIndex: 1000,
                    scroll: false,
                    containment: "parent",
                    revert: "invalid"
                },
                preventRecursiveMoves: true, // Prevent dropping nodes on own descendants
                preventVoidMoves: true, // Prevent dropping nodes 'before self', etc.

                dragStart: function (node, data) {
                    current_parent = node.parent.key
                    return true;
                },
                dragEnter: function (node, data) {
                    return true;
                },
                dragExpand: function (node, data) {
                    // return false to prevent auto-expanding data.node on hover
                },
                dragOver: function (node, data) {
                },
                dragLeave: function (node, data) {
                },
                dragStop: function (node, data) {
                },
                dragDrop: function (node, data) {
                    data.otherNode.moveTo(node, data.hitMode);

                    iziToast.show({
                        theme: 'dark',
                        icon: 'icon-person',
                        title: gettext('Move Element'),
                        message: gettext('Are you sure make this move?'),
                        position: 'bottomCenter',
                        progressBarColor: 'rgb(0, 255, 184)',
                        buttons: [
                            ['<button>Ok</button>', function (instance, toast) {
                                getAjaxCall(Urls[url]({node_from_id: data.otherNode.key, node_to_id: node.key, action: data.hitMode })),
                                instance.hide(toast, {transitionOut: 'fadeOut'}, 'button');
                            }, true], // true to focus
                            ['<button>' + gettext("Cancel") + '</button>', function (instance, toast) {
                                location.reload();
                            }]
                        ],
                        onClosing: function(instance, toast, closedBy){
                            if(closedBy == 'timeout'){
                                getAjaxCall(Urls[url]({node_from_id: data.otherNode.key, node_to_id: node.key, action: data.hitMode }))
                            }
                        },
                    });

                    $("#treegrid").fancytree("getTree").visit(function (node) {
                        node.setExpanded();
                    });
                }
            },
        });

        current_parent = '';
        fancytree.fancytree("getTree").visit(function (node) {
            node.setExpanded();
        });
}


function getAjaxCall(url) {
    $.get(url, function (data) {
        console.log("success");
        return data;
    })
        .done(function () {
        })
        .fail(function () {
            console.log("error");
        })
}