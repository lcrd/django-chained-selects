(function($) {
    $(document).ready(function(){
        function get_initial_value($select) {
            var val = $select.val();
            if (!val) {
                val = $select.data('initial');
                if (typeof val === 'undefined') {
                    console.error(
                        $select.attr('name') + ' ' +
                        'initial value could not be found')
                    return ''
                };
            };
            return val
        }

        function fill_empty(target, label) {
            options = '<option value="">' + label + '</option>';
            target.html(options);
            target.find('option:first').attr('selected', 'selected');
            target.trigger('change');
        }

        function fill_field(target, label, url, pk, initial_value) {
            $.getJSON(url + pk + '/', function(j) {
                var options = '<option value="">' + label + '</option>';
                for (var i = 0; i < j.length; i++) {
                    options += '<option value="' + j[i].value + '">' + j[i].display + '</option>';
                }
                var width = target.outerWidth();
                target.html(options);
                if (navigator.appVersion.indexOf("MSIE") != -1)
                    target.width(width + 'px');
                target.find('option:first').attr('selected', 'selected');
                var auto_choose = true;

                if(initial_value){
                    target.find('option[value="'+ initial_value +'"]').attr('selected', 'selected');
                }
                if(auto_choose && j.length == 1){
                    target.find('option[value="'+ j[0].value +'"]').attr('selected', 'selected');
                }
                target.trigger('change');
            })
        }

        // find parent select and assign handlers
        $('select.chained').each(function() {
            var $parent = $('#' + $(this).data('parent-id')),
                $target = $(this),
                url = $(this).data('url'),
                empty_label = $(this).data('empty-label');

            $parent.on('change', function() {

                var pk = $(this).val();
                if (!pk || pk == '')
                    fill_empty($target, empty_label);
                else {
                    var initial_value = get_initial_value($target);
                    if (initial_value != '')
                        fill_field($target, empty_label, url, pk, initial_value);
                    else
                        fill_field($target, empty_label, url, pk);
                }
            });
            // parent field initial key
            var pk = get_initial_value($parent);
            // new record
            if (typeof pk === 'undefined')
                fill_empty($target, empty_label);
            // get edit record initial value
            else {
                var initial_value = $target.data('initial');
                if (typeof initial_value !== 'undefined')
                    fill_field($target, empty_label, url, pk, initial_value);
            }
        });
    });
})(jQuery || django.jQuery);
