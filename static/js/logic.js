d3.json("/api/v1.0/data").then((data)=>{
  // console.log(data)

  // Define sections of data
  var avo_prices = data.avocado_prices
  var gas_prices = data.gas_prices
  var tot_transport = data.tot_transport
  var avo_transport = data.avo_transport
  var weather = data.weather
  var weather2 = data.weather2
  var bananas = data.bananas
  // console.log(avo_prices)
  // console.log(gas_prices)
  // console.log(tot_transport)
  // console.log(avo_transport)
  // console.log(weather)
  // console.log(bananas)

  // initialize charts for rewriting with input data
  function init() {
    
    // Set up chart
    var trace = {
      x: [],
      y: [],
      mode: 'markers',
      marker: {
        size: []
      }
    };
    
    var data = [trace];
    
    var layout = {
      title: 'Charts',
      showlegend: false,
    };
    
    var chart = d3.selectAll("#chart").node();
    
    Plotly.newPlot(chart, data, layout);
  }

  // -- TRANSPORT DATA FUNCTIONS AND INFO --
  d3.selectAll(".avocado__skin").on("click", transport);

  function transport() {
    // console.log("it worked");

    // replotting transport visualizations
    

    // grab nodes for updating info card
    var dashboard_title = d3.select("#dashboard_title");
    var dashboard_subTitle = d3.select("#dashboard_subtitle");
    var dashboard_text = d3.select("#dashboard_text");
    
    // Update info card with new text
    dashboard_title.text("USDA Transport Data");
    dashboard_subTitle.text("Trucking Availability and Rates");
    dashboard_text.text("This data comes from the USDA Ag Transport site ( https://agtransport.usda.gov/ ), specifically the trucking category. This data shows the availability and rates for refrigerated trucks transporting ag commodities and we utilized this and were able to drill down to see costs associated specifically with avocados.");

  };
  // -- TRANSPORT DATA FUNCTIONS AND INFO --

  init();

});
