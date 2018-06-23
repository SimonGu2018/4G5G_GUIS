
//Tput data display
function tputBar(ullist, dllist) {
	Highcharts.chart('container', {
  	credits: {  
    	enabled: false
    	//text: 'www.ericsson.com',
    	//href: 'https://www.ericsson.com/', 
  	}, 
  	exporting: {
    	enabled: false
  	},
  	chart: {
    	type: 'column'
  	},
  	title: {
      //enabled: false
    	text: 'TM500 Tput Realtime Data (MByte/s)',
      style:{
        //color: '#3E576F',
        fontSize: '12px'
      }
  	},
  	//subtitle: {
    //	text: 'Source: TM500 Tput Realtime Data (MByte/s)'
  	//},
  	xAxis: {
  		categories: [
    		'TM-1',
    		'TM-2',
    		'TM-3',
    		'TM-4',
    		'TM-5',
    		'TM-6',
    		'TM-7',
    		'TM-8',
  		],
  		crosshair: true
  	},
  	yAxis: {
  		min: 0,
  		title: {
        enabled: false
    		//text: 'Throughtput(MByte/s)'
   		},
  		//tickInterval: 50
      labels:{
        enabled: false
      }
  	},
    tooltip: {
		  headerFormat: '<span style="font-size:8px">{point.key}</span><table>',
    	pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
        '<td style="padding:0"><b>{point.y:.1f} MB</b></td></tr>',
    	footerFormat: '</table>',
    	shared: true,
    	useHTML: true
  	},
  	plotOptions: {
    	column: {
      	pointPadding: 0.2,
      	borderWidth: 0,
      	dataLabels: {
        	enabled: true,
          formatter: function() {
            console.log(this.y)
            if (this.y == 0) {
              return null;
            } else {
                return this.y;
              }
          }
      	},
      	style: {
        	shadow: false
      	}
  	  },
  	  series: {
    	  animation: false,
        pointWidth: 15,
        pointPadding: 0,
        groupPadding: 0
  	  }
	  },
  	series: [{
    	name: 'Uplink',
    	color:'#50B432',
    	data: ullist
		}, {
    		name: 'Downlink',
    		color:'#058DC7',
    		data: dllist
  	}]
  });
};

function randomint(min, max, num){  
	var ranlist = [];
	for (var i=0; i<num; i++) {
  	ranlist.push(Math.floor(Math.random() * (max- min) + min));
	} 
	return ranlist;   
}  

//---------------- Load Function ----------------
function adddLoadEvent(func){
	var oldonload = window.onload;
	if (typeof window.onload != "function") {
  	window.onload = func;
	} else {
  	window.onload = function(){
  		oldonload();
  		func();
		}
	}
}

