var chartBasic = (function (ele, arr, options) {
    var initArray = arr;
    var initOptions = options;
    var chartElement = document.getElementById(ele);

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

    function setOptions(options) {
        initOptions = getOptions(options);
    }

    function setGroupWidth(options, arr) {
        options.bar = Object.assign({}, options.bar, {groupWidth: options.width / getArray(arr).length});
    }

    function draw(arr, options) {
        var data = convertData(arr);
        var options = getOptions(options);

        setGroupWidth(options, arr);

        chart = new google.visualization.ColumnChart(chartElement);
        chart.draw(data, options);
    }

    function setArray (arr) {
        initArray = getArray(arr);
    }

    function swap (i, j) {
        var temp = initArray[i];
        initArray [i] = initArray[j];
        initArray[j] = temp;

        draw();
    }

    function smaller(i, j) {
        return initArray[i] < initArray[j];
    }

    function larger(i, j) {
        return initArray[i] > initArray[j];
    }
    
    return {
        draw,
        setOptions,
        setArray,
        swap,
        smaller,
        larger
    }
});