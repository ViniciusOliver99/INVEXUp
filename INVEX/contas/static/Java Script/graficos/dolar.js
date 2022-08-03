const ctx = document.getElementById('grafico')

const labels = [

    '2010',
    '2011',
    '2012',
    '2013',
]

const data = {
    labels,
    datasets:[{
        data: [456,642,6,654],
        label:"Gráfico"
    }]
}

const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true
    }
  };

  const grafico = new Chart(ctx, config)