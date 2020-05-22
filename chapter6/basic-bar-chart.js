var chartBasic = (function (ele, pele, arr, options) {
    var initArray = arr;
    var initOptions = options;
    var chartElement = document.getElementById(ele);
    var progressElement = document.getElementById(pele);

    var defaultStyle = 'stroke-color: #312ab5; stroke-width: 1; fill-color: #3864f5';
    var compareStyle = 'stroke-color: #312ab5; stroke-width: 1; fill-color: #30fca4';
    var largerStyle = 'stroke-color: #312ab5; stroke-width: 1; fill-color: #f930fc';
    var smallerStyle = 'stroke-color: #312ab5; stroke-width: 1; fill-color: #effc30';

    function getArray(arr) {
        if(arr === undefined || arr === null)
            arr = initArray;
        return arr;
    }

    function convertData(arr, iOption, jOption) {
        var data = getArray(arr).map(x => ['', x, defaultStyle]);
        if(iOption !== undefined && iOption === null)
            data[iOption.index][2] = iOption.style;
        if(jOption !== undefined && jOption === null)
            data[jOption.index][2] = jOption.style;
        data.unshift(['', '', { role: 'style' }]);
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

    function draw(iOption, jOption) {
        var data = convertData(null, iOption, jOption);
        var options = getOptions();

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
        progressElement.innerText = `Comparing ${i} and ${j} element`;
        var iOption = { index: i, style: compareStyle };
        var jOption = { index: j, style: compareStyle };
        draw(iOption, jOption);
        // sleep(100);

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