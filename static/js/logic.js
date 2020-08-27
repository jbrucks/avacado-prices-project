d3.json("/api/v1.0/data").then((data)=>{
  // console.log(data)

  // Define sections of data
  var avo_prices = data.avocado_prices
  var gas_prices = data.gas_prices
  var tot_transport = data.tot_transport
  var avo_transport = data.avo_transport
  var weather = data.weather
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
      title: 'Chart',
      showlegend: false,
    };
    
    var chart = d3.selectAll("#chart");
    
    Plotly.newPlot(chart, data, layout);
  }

  d3.selectAll(".avocado").on("click", transport);

  // -- TRANSPORT DATA FUNCTIONS AND INFO --
  function transport() {
    console.log("it worked");
    var dashboard_title = d3.selectAll(".dashboard_title").node();
    var dashboard_subTitle = d3.selectAll(".dashboard_subtitle").node();
    var dashboard_text = d3.selectAll(".dashboard_text").node();
    Object.entries(dashboard_title).append().attr("value", "USDA Transport Data");
    Object.entries(dashboard_subTitle).append().attr("value", "Trucking Availability and Rates");
    Object.entries(dashboard_text).append().attr("value", "This data comes from the USDA site (https://agtransport.usda.gov/). Specifically the trucking category. This data shows the availability and rates for refrigerated trucks transporting ag commodities and we utilized this and were able to drill down to see costs associated specifically with avocados.");
  };
  // -- TRANSPORT DATA FUNCTIONS AND INFO --

  init();

});
