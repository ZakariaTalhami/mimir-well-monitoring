import { Component, Input, OnInit } from '@angular/core';
import { FireUpService } from '../../services/fire-up.service';
import { Well } from '../../models/well';
import { Observable } from 'rxjs'

@Component({
  selector: 'card-comp',
  templateUrl: 'cards.component.html'
})
export class CardsComponent  implements OnInit{

  wells: Well[];
  @Input() wellID: string;
  reading: number;
  volume: number;

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
    this.wellDAO.getReadings(this.wellID).subscribe(data =>{
          // console.log(data);
          let levels = data.map(item => item.Level);
          let vol = data.map(item => item.Volume);
          // console.log(levels);
          this.reading = levels.pop();
          this.volume = vol.pop();
        } );
  }

}
