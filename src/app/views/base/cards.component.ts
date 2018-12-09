import { Component, Input, OnInit } from '@angular/core';
import { FireUpService } from '../../services/fire-up.service';
import { Well } from '../../models/well';
import { Observable } from 'rxjs'
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';

@Component({
  selector: 'card-comp',
  templateUrl: 'cards.component.html'
})
export class CardsComponent  implements OnInit{

  wells: Well[];
  @Input() wellID: string;
  @Input() wellName: string;
  reading: number;
  volume: number;

  public avgs: Array<number> = [];
  public lineChart1Data: Array<any> = [
    {
      data: this.avgs,
      label: 'Series A'
    }
  ];
  public avgsLabels: Array<any> = [];
  // public avgsLabels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public avgsOptions: any = {
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
  public avgsColours: Array<any> = [
    {
      backgroundColor: getStyle('--primary'),
      borderColor: 'rgba(255,255,255,.55)'
    }
  ];
  public avgsLegend = false;
  public avgsType = 'line';

  temp:Observable<Well>;

  constructor(private wellDAO: FireUpService)  {
    // console.log(this.wellID);
    


    // this.wellDAO.getWells().subscribe(item => {
    //   console.log(item);
      
    //   this.wells = item;   
    //   this.wellID = item.pop().id

    //   this.wellDAO.getReadings(this.wellID).subscribe(data =>{
    //     console.log(data);
    //     let levels = data.map(item => item.Level);
    //     let vol = data.map(item => item.Volume);
    //     console.log(levels);
    //     this.reading = levels.pop();
    //     this.volume = vol.pop();
    //   } );
      
    // });
  }

  ngOnInit(){
    console.log("Card of "+this.wellID);
    
    this.wellDAO.getReadings(this.wellID).subscribe(data =>{
          // console.log(data);
          let levels = data.map(item => item.Level);
          let vol = data.map(item => item.Volume);
          // console.log(levels);
          this.reading = levels.pop();
          this.volume = vol.pop();
        } );

    this.wellDAO.getArchivedStats(this.wellID).subscribe(data=> {
      console.log("stats of "+this.wellID);
      console.log(data);
      this.avgsLabels = data.map(stats => stats.id) 
      this.lineChart1Data[0].data = data.map(stats => stats.Avg)     
      
    });
  }

}
