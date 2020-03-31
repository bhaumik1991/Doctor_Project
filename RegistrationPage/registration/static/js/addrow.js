$(document).ready(function () {
    var counter = 0;

    $("#addrow").on("click", function () {
        var newRow = $("<tr>");
        var cols = "";

        cols += '<td><input type="text" class="form-control" name="type' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="mediciene_name' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="mediciene_power' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="does' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="days' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="comments' + counter + '"/></td>';


        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger "  value="Delete"></td>';
        newRow.append(cols);
        $("table.order-list").append(newRow);
        counter++;
    });



    $("table.order-list").on("click", ".ibtnDel", function (event) {
        $(this).closest("tr").remove();
        counter -= 1
    });


});


