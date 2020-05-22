var bubbleSort = (function() {

    var chart = null;
    var data = [10, 1, 9, 3, 6, 4, 2, 5, 8, 7];

    function init() {
        var options = {title: 'Bubble title'};

        chart = chartBasic('bubble-sort', data, options);
        chart.draw();
    }


    function sort() {
        for (var i = 0; i < data.length; i++) {
            for (var j = 0; j < data.length - i; j++) {
                if (chart.larger(j, j + 1))
                    chart.swap(j, j + 1);
            }
        }
    }

    return {
        init,
        sort
    }
});