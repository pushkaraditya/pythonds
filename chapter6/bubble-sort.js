var bubbleSort = (function() {
    var options = {title: 'Customized title'};
    var arr = [2,5,3,6,5];
    var ele = document.getElementById('chart');

    console.log(chartBasic(arr, options).draw(ele));
});