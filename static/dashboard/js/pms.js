
function orderfd(k, id) {
    var quantity = $("#quantity"+k).val();
    // alert(quantity)
    $.ajax({
        type : 'GET',
        url : "/orderfood/",
        data : {
            quantity : quantity,
            id:id,
        },
        dataType: 'json',
        success : function(data)
        {
            cart = '' 
            for(oi in data) {
                cart += '<tr><td>' + data[oi].name + '</td><td>' + data[oi].price + ' </td><td>' + data[oi].qty + '</td><td>'+ data[oi].total +'<td><button class="btn-styled" type="submit" onclick="deleteitem(' + data[oi].id + ')">Delete</button></td></tr>'
            }
            $('#cartitemstbl').html(cart);
            $('#cartitemsmdl').modal('show');
        }
    })
}

function cartconfirm()
{
    $.ajax({
        type : 'GET',
        url : "/cartconfirm/",
        dataType: 'json',
        success : function(data)
        {
            cart = '' 
            for(oi in data) {
                cart += '<tr><td>' + data[oi].name + '</td><td>' + data[oi].price + ' </td><td>' + data[oi].qty + '</td><td>'+ data[oi].total +'<td><button class="btn-styled" type="submit" onclick="deleteitem(' + data[oi].id + ')">Delete</button></td></tr>'
            }
            $('#cartitemstbl').html(cart);
            $('#cartitemsmdl').modal('show');

        }
    })

}


function deleteitem(id)
{
    
    $.ajax({
        type : 'GET',
        url : '/deleteitem/',
        data : {
            di_id : id,

        },
        dataType: 'json',
        success : function(data)
        {
            alert("Delete item")
            window.location.reload()
        }

    })
}

function approveorder(id) {
    
    $.ajax({
        type : 'GET',
        url : "/approveorder/",
        data : {
            id : id,
        },
        dataType : 'json',
        success : function(data)
        {
     
            $('#status'+id).html(data.status)
            window.location.reload()
        }
    })
}

function orderpacked(id){
    $.ajax({
        type : 'GET',
        url : "/orderpacked/",
        data : {
            id : id,
        },
        dataType : 'json',
        success : function(data)
        {
          
            $('#status'+id).html(data.status)
            window.location.reload()
        }
    })
}

function orderondelivery(id){
    $.ajax({
        type : 'GET',
        url : "/orderondelivery/",
        data : {
            id : id,
        },
        dataType : 'json',
        success : function(data)
        {    
            $('#status'+id).html(data.status)
            window.location.reload()
        }
    })
}

function orderdelivered(id){
    $.ajax({
        type : 'GET',
        url : "/orderdelivered/",
        data : {
            id : id,
        },
        dataType : 'json',
        success : function(data)
        {    
            $('#status'+id).html(data.status)
            window.location.reload()
        }
    })
}

function adm_cancelodr(id){
    $.ajax({
        type : 'GET',
        url : "/adm_cancelodr/",
        data : {
            cl_id : id,
        },
        dataType : 'json',
        success : function(data)
        {    
            // $('#status'+id).html(data.status)
            window.location.reload()
        }
    })
}

function adminviewordereditem(id) {
    
    $.ajax({
        type : 'GET',
        url : "/adminviewordereditem/",
        data : {
            od_id : id,
        },
        dataType : 'json',
        success : function(data)
        {
            // alert("Order approved")
            items = ''
            for(oi in data) {
                items += '<tr><td>' + data[oi].name + '</td><td>' + data[oi].price + ' </td><td>' + data[oi].qty + '</td><td>'+ data[oi].total +'</td></tr>'
            }
            $('#p_orderitems').html(items);
            $('#view_orderitems').modal('show');
        }
    })
}

function cancelorder(id){
    $.ajax({
        type : 'GET',
        url : "/patient/cancelorder/",
        data : {
            id : id,
        },
        dataType : 'json',
        success : function(data)
        {
            alert("Order canceled")
            window.location.reload()
        }
    })

}
