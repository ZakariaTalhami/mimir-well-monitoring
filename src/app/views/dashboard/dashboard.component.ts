import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { FireUpService } from '../../services/fire-up.service';
import { Well } from '../../models/well';
import { reading } from '../../models/reading';

@Component({
  templateUrl: 'dashboard.component.html'
})
export class DashboardComponent implements OnInit {
  wellLoaded: boolean = false;
  wells:Well[];
  readings: reading[];
  readingList={};
  wellID:string;


  radioModel: string = 'Month';
  deleteMe: string = 'hola';

  // lineChart1
  public lineChart1Data: Array<any> = [
    {
      data: [65, 59, 84, 84, 51, 55, 40],
      label: 'Series A'
    }
  ];
  public lineChart1Labels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public lineChart1Options: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips
    },
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        gridLines: {
          color: 'transparent',
          zeroLineColor: 'transparent'
        },
        ticks: {
          fontSize: 2,
          fontColor: 'transparent',
        }

      }],
      yAxes: [{
        display: false,
        ticks: {
          display: false,
          min: 40 - 5,
          max: 84 + 5,
        }
      }],
    },
    elements: {
      line: {
        borderWidth: 1
      },
      point: {
        radius: 4,
        hitRadius: 10,
        hoverRadius: 4,
      },
    },
    legend: {
      display: false
    }
  };
  public lineChart1Colours: Array<any> = [
    {
      backgroundColor: getStyle('--primary'),
      borderColor: 'rgba(255,255,255,.55)'
    }
  ];
  public lineChart1Legend = false;
  public lineChart1Type = 'line';

  // lineChart2
  public lineChart2Data: Array<any> = [
    {
      data: [1, 18, 9, 17, 34, 22, 11],
      label: 'Series A'
    }
  ];
  public lineChart2Labels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public lineChart2Options: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips
    },
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        gridLines: {
          color: 'transparent',
          zeroLineColor: 'transparent'
        },
        ticks: {
          fontSize: 2,
          fontColor: 'transparent',
        }

      }],
      yAxes: [{
        display: false,
        ticks: {
          display: false,
          min: 1 - 5,
          max: 34 + 5,
        }
      }],
    },
    elements: {
      line: {
        tension: 0.00001,
        borderWidth: 1
      },
      point: {
        radius: 4,
        hitRadius: 10,
        hoverRadius: 4,
      },
    },
    legend: {
      display: false
    }
  };
  public lineChart2Colours: Array<any> = [
    { // grey
      backgroundColor: getStyle('--info'),
      borderColor: 'rgba(255,255,255,.55)'
    }
  ];
  public lineChart2Legend = false;
  public lineChart2Type = 'line';


  // lineChart3
  public lineChart3Data: Array<any> = [
    {
      data: [78, 81, 80, 45, 34, 12, 40],
      label: 'Series A'
    }
  ];
  public lineChart3Labels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public lineChart3Options: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips
    },
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        display: false
      }],
      yAxes: [{
        display: false
      }]
    },
    elements: {
      line: {
        borderWidth: 2
      },
      point: {
        radius: 0,
        hitRadius: 10,
        hoverRadius: 4,
      },
    },
    legend: {
      display: false
    }
  };
  public lineChart3Colours: Array<any> = [
    {
      backgroundColor: 'rgba(255,255,255,.2)',
      borderColor: 'rgba(255,255,255,.55)',
    }
  ];
  public lineChart3Legend = false;
  public lineChart3Type = 'line';


  // barChart1
  public barChart1Data: Array<any> = [
    {
      data: [78, 81, 80, 45, 34, 12, 40, 78, 81, 80, 45, 34, 12, 40, 12, 40],
      label: 'Series A'
    }
  ];
  public barChart1Labels: Array<any> = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'];
  public barChart1Options: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips
    },
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        display: false,
        barPercentage: 0.6,
      }],
      yAxes: [{
        display: false
      }]
    },
    legend: {
      display: false
    }
  };
  public barChart1Colours: Array<any> = [
    {
      backgroundColor: 'rgba(255,255,255,.3)',
      borderWidth: 0
    }
  ];
  public barChart1Legend = false;
  public barChart1Type = 'bar';

  // mainChart

  public mainChartElements = 27;
  public mainChartData1: Array<number> = [];
  public mainChartData2: Array<number> = [];
  public mainChartData3: Array<number> = [];

  // public mainChartData: Array<any> = [];
  public mainChartData: Array<any> = [
    {
      data: this.mainChartData1,
      label: 'Level'
    },
    {
      data: this.mainChartData2,
      label: 'Volume'
    },
    // {
    //   data: this.mainChartData3,
    //   label: 'BEP'
    // }
  ];
  /* tslint:disable:max-line-length */
  // public mainChartLabels: Array<any> = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Thursday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    public mainChartLabels: Array<any> = [];
  /* tslint:enable:max-line-length */
  public mainChartOptions: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips,
      intersect: true,
      mode: 'index',
      position: 'nearest',
      callbacks: {
        labelColor: function(tooltipItem, chart) {
          return { backgroundColor: chart.data.datasets[tooltipItem.datasetIndex].borderColor };
        },
        title: function(items , data){
          console.log(items , data);
          // console.log(data.labels[items.index]);
          let stamp = data.labels[items[0].index];
          return data.labels[items[0].index];
          // return stamp.getFullYear()+":"+stamp.getMonth()+":"+stamp.getDate()+" "+items[0].xLabel ;
        }
      }
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        display:true,
        gridLines: {
          drawOnChartArea: true,
        },
        ticks: {
          callback: function(value: any) {
            return value.getHours()+":"+value.getMinutes();
          }
        }
      }],
      yAxes: [{
        // ticks: {
        //   beginAtZero: true,
        //   maxTicksLimit: 5,
        //   stepSize: Math.ceil(250 / 5),
        //   max: 250
        // }
      }]
    },
    elements: {
      line: {
        borderWidth: 2
      },
      point: {
        radius: 0,
        hitRadius: 10,
        hoverRadius: 4,
        hoverBorderWidth: 3,
      }
    },
    legend: {
      display: false
    }
  };
  public mainChartColours: Array<any> = [
    { // brandInfo
      backgroundColor: hexToRgba(getStyle('--info'), 10),
      borderColor: getStyle('--info'),
      pointHoverBackgroundColor: '#fff'
    },
    { // brandSuccess
      // backgroundColor: 'transparent',
      backgroundColor: hexToRgba(getStyle('--success'), 10),
      borderColor: getStyle('--success'),
      pointHoverBackgroundColor: '#fff'
    },
    { // brandDanger
      backgroundColor: 'transparent',
      borderColor: getStyle('--danger'),
      pointHoverBackgroundColor: '#fff',
      borderWidth: 1,
      borderDash: [8, 5]
    }
  ];
  public mainChartLegend = false;
  public mainChartType = 'line';

  // social box charts

  public brandBoxChartData1: Array<any> = [
    {
      data: [65, 59, 84, 84, 51, 55, 40],
      label: 'Facebook'
    }
  ];
  public brandBoxChartData2: Array<any> = [
    {
      data: [1, 13, 9, 17, 34, 41, 38],
      label: 'Twitter'
    }
  ];
  public brandBoxChartData3: Array<any> = [
    {
      data: [78, 81, 80, 45, 34, 12, 40],
      label: 'LinkedIn'
    }
  ];
  public brandBoxChartData4: Array<any> = [
    {
      data: [35, 23, 56, 22, 97, 23, 64],
      label: 'Google+'
    }
  ];

  public brandBoxChartLabels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public brandBoxChartOptions: any = {
    tooltips: {
      enabled: false,
      custom: CustomTooltips
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        display: false,
      }],
      yAxes: [{
        display: false,
      }]
    },
    elements: {
      line: {
        borderWidth: 2
      },
      point: {
        radius: 0,
        hitRadius: 10,
        hoverRadius: 4,
        hoverBorderWidth: 3,
      }
    },
    legend: {
      display: false
    }
  };
  public brandBoxChartColours: Array<any> = [
    {
      backgroundColor: 'rgba(255,255,255,.1)',
      borderColor: 'rgba(255,255,255,.55)',
      pointHoverBackgroundColor: '#fff'
    }
  ];
  public brandBoxChartLegend = false;
  public brandBoxChartType = 'line';

  constructor(private wellService: FireUpService){

  }

  public random(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  ngOnInit(): void {
    // generate random values for mainChart
    this.wellService.getWells().subscribe(item => {
        // console.log(item);
        this.wells = item;  
        this.wellLoaded = true;
        this.wellID = this.wells[0].id
        console.log("pizza and candy");
        console.log(this.wellID);
        console.log("pizza and candy");
        
        if (this.wells.length < 0){ return }

      //   this.wellService.getReadings(this.wellID).subscribe(res => {
      //     console.log("Burger");
      //     console.log(this.wellID);
      //     console.log("Burger");
      //     this.readingList[this.wellID] = res;
      //     this.readings = res;
      //     this.mainChartLabels = this.readings.map(res => new Date(res.Timestamp.seconds));
      //     this.mainChartData[0].data = this.readings.map(res => res.Level);
      //     this.mainChartData[1].data = this.readings.map(res => res.Volume);
      // })

      for (let i = 0; i < this.wells.length; i++) {
        const well = this.wells[i];
        console.log(well);

        this.wellService.getReadings(well.id).subscribe(res => {
            this.readingList[well.id] = res;
            if(well.id == this.wellID){
              this.readings = res;
              this.mainChartLabels = this.readings.map(res => new Date(res.Timestamp.seconds));
              this.mainChartData[0].data = this.readings.map(res => res.Level);
              this.mainChartData[1].data = this.readings.map(res => res.Volume);
            }
        })

      }
      
    });

    // this.wellService.getReadings('Well_1').subscribe(res => {
    //     this.readings = res;
    //     this.mainChartLabels = this.readings.map(res => new Date(res.Timestamp.seconds));
    //     this.mainChartData[0].data = this.readings.map(res => res.Level);
    // })

    // for (let i = 0; i <= this.mainChartElements; i++) {
    //   this.mainChartData1.push(this.random(50, 200));
    //   this.mainChartData2.push(this.random(80, 100));
    //   this.mainChartData3.push(65);
    // }

    // console.log('in the Dash');
    // console.log(this.wells);
    
    
  }


  downloadReading(){
    // console.log('downloadReading');
    let csvContent = "data:text/csv;charset=utf-8,Level,Volume,Timestamp,\r\n";
    // console.log(this.mainChartData[0].data);
    
    this.readings.forEach(function(reading){
      // console.log(reading);
      let row = reading.Level+","+reading.Volume+","+(new Date(reading.Timestamp.seconds))
      // Error this is an object
      // row = arr.join(",");
      csvContent += row + "\r\n";
    }); 
    // console.log(csvContent);
    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "my_data.csv");
    document.body.appendChild(link); // Required for FF

    link.click(); // This will download the data file named "my_data.csv".
    
  }


  changeChart(event: any){
    var target = event.currentTarget;
    const id = target.attributes.id.nodeValue;
    this.wellID = id;   
    console.log(id);
    console.log(this.readingList[id]);
    this.readings = this.readingList[id];
    // let arr = this.readingList[id]
    this.mainChartLabels = this.readings.map(res => new Date(res.Timestamp.seconds));
    this.mainChartData[0].data = this.readings.map(res => res.Level);
    this.mainChartData[1].data = this.readings.map(res => res.Volume);
  }
}
