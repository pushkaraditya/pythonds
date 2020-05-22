var chartBasic = (function (arr, options) {
    var initArray = arr;
    var initOptions = options;

    function getArray(arr) {
        if(arr === undefined)
            arr = initArray;
        return arr;
    }

    function convertData(arr) {
        var data = getArray(arr).map(x => ['', x]);
        data.unshift(['', '']);
        return new google.visualization.arrayToDataTable(data);
    }

    function getOptions(options) {
        var defaultOptions = {
            title: 'Sorting Charts',
            legend: 'none',
            height: 200,
            width: 400
        };
        return Object.assign(defaultOptions, initOptions, options);
    }

    function setGroupWidth(options, arr) {
        options.bar = Object.assign({}, options.bar, {groupWidth: options.width / getArray(arr).length});
    }

    function draw(ele, arr, options) {
        var data = convertData(arr);
        var options = getOptions(options);

        setGroupWidth(options, arr);

        chart = new google.visualization.ColumnChart(ele);
        chart.draw(data, options);
    }
    
    return {
        draw,
        convertData
    }
});