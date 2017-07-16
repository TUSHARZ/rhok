window.onload = function () {

      var dps = [{y:30.45 , x: 1999}, {y: 32.37, x: 2000}, {y: 33.76, x: 2001}, {y: 34.9, x: 2002}, {y: 39.13, x: 2003},{y: 41.36, x: 2004}, {y: 44.35, x: 2005}, {y: 46.34, x: 2006}, {y: 49.19, x: 2007}, {y: 50.97, x: 2008}];   //dataPoints. 

      var chart = new CanvasJS.Chart("chartContainer",{
        title :{
          text: "Radiations according to year"
        },
        axisX: {            
          title: "Year"
        },
        axisY: {            
          title: "Radiations"
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

 
}
       