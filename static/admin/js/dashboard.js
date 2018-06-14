
$('#chart_1').highcharts({
    chart: {
        type: 'pie',
        plotBackgroundColor: null,
        plotBorderWidth: 0,
        plotShadow: false,
        marginTop: -0,
            marginBottom: -40,
            marginLeft: -70,
            marginRight: -30
    },
    title: {
        text: 'Total de Pedidos',
        align: 'center',
        verticalAlign: 'top',
       
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            dataLabels: {
                enabled: true,                    
                style: {
                    fontWeight: 'bold',
                    color: 'black',
                }
            },
            size: '100%',
            startAngle: -90,
            endAngle: 90,
            center: ['50%', '75%']
        }
    },
    colors: ['#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4'],
    series: [{
        type: 'pie',
        size: '100%',
        name: 'Browser share',
        marginTop:0,
        marginLeft:-100,
        innerSize: '50%',
        data: [
            ['Firefox',   45.0],
            ['IE',       26.8],
            ['Chrome', 12.8],

        ]
    }]
});


Highcharts.chart('chart_2', {
    chart: {
        type: 'pie',
        spacingBottom: 0,
        paddingTop: 10,
        options3d: {
            enabled: true,
            alpha: 45
        }
    },
    title: {
        text: 'Total de Ventas'
    },
    subtitle: {
        text: ''
    },
    plotOptions: {
        pie: {
            innerSize: 100,
            depth: 45
        }
    },
    colors: ['#7cb5ec', '#f7a35c', '#90ee7e', '#7798BF', '#aaeeee', '#ff0066',
        '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    series: [{
        name: 'Delivered amount',
        data: [
            ['Bananas', 8],
            ['Kiwi', 3],
            ['Mixed nuts', 1],

        ]
    }]
});

