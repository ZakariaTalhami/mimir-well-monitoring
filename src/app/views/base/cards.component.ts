import { Component } from '@angular/core';
import { FireUpService } from '../../services/fire-up.service';
import { Well } from '../../models/well';
import { reading } from '../../models/reading';

@Component({
  selector: 'card-comp',
  templateUrl: 'cards.component.html'
})
export class CardsComponent {

  wells: Well[];
  wellID: string;
  reading: number;
  volume: number;

  constructor(private wellDAO: FireUpService) {
    this.wellDAO.getWells().subscribe(item => {
      console.log(item);
      
      this.wells = item;   
      this.wellID = item.pop().id

      this.wellDAO.getReadings(this.wellID).subscribe(data =>{
        console.log(data);
        let levels = data.map(item => item.Level);
        let vol = data.map(item => item.Volume);
        console.log(levels);
        // let times = data.map(item => {
        //   let x = new Date();
        //   x.setSeconds(item.Timestamp.seconds);
        //   return x;
        // });
        this.reading = levels.pop();
        this.volume = vol.pop();
        // console.log(times);
      } );
      
    });
  }

}
