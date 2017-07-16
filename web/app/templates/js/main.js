window.onload = function () {

      var dps = [{x:30.45 , y: 1999}, {x: 32.37, y: 2000}, {x: 33.76, y: 2001}, {x: 34.9, y: 2002}, {x: 39.13, y: 2003},{x: 41.36, y: 2004}, {x: 44.35, y: 2005}, {x: 46.34, y: 2006}, {x: 49.19, y: 2007}, {x: 50.97, y: 2008}];   //dataPoints. 

      var chart = new CanvasJS.Chart("chartContainer",{
        title :{
          text: "Radiations according to year"
        },
        axisX: {            
          title: "Radiations"
        },
        axisY: {            
          title: "Year"
        },
        data: [{
          type: "line",
          dataPoints : dps
        }]
      });

      chart.render();
      var xVal = dps.length + 1;
      var yVal = 15;  
      var updateInterval = 1200;

      var updateChart = function () {
        
        
        yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
        dps.push({x: xVal,y: yVal});
        
        xVal++;
        if (dps.length >  10 )
        {
          dps.shift();        
        }

        chart.render();   

  // update chart after specified time. 

};

setInterval(function(){updateChart()}, updateInterval); 
}
       