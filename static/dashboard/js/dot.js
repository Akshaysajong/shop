
// $(document).ready(function()
// {
// var country = $("#country");
// var state = $("#state");
// var city = $('#city');
// var $options = state.find('option');

// country.on('change',function(){
//         state.html($options.filter('[value="'+ this.value +'"]'));
//     }).trigger('change');
// });

function  get_country(){
    jQuery.ajax({
        type: 'get',
        url: "/ajax_country/",
        data:{
            'country':$('#country').val()
        },
        dataType: 'json',
        success: function(data)
        {
            var op = '<option value="">--Select--</option>' 
            for(st in data){
                op += '<option value="'+data[st].id+'">'+ data[st].name + '</option>' 
            }
            $('#state').html(op)

        }
    })
}


function get_state()
{

    jQuery.ajax({
        type: 'get',
        url: "/ajax_state/",
        data:{
            'state' : $('#state').val()
        },
        dataType: 'json',
        success: function(data)
        {
            var op = '<option value="">--Select--</option>' 
            for(st in data){
                op += '<option value="'+data[st].id+'">'+ data[st].name + '</option>' 
            }
            $('#city').html(op)

        }
    })

}