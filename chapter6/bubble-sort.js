var bubbleSort = (function() {

    var chart = null;
    var originalData = [10, 1, 9, 3, 6, 4, 2, 5, 8, 7];
    var data = copyArray(originalData);

    function init() {
        var options = {title: 'Bubble Sort'};

        chart = chartBasic('bubble-sort', 'bubble-sort-progress', data, options);
        chart.draw();
    }
    
    function reset() {
        data = copyArray(originalData);
        chart.setArray(data);
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
        reset,
        sort
    }
});