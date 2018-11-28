import { Injectable } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection , AngularFirestoreDocument  } from 'angularfire2/firestore';
import { importType } from '@angular/compiler/src/output/output_ast';
import { Well } from '../models/well';
import { reading } from '../models/reading';
import { Observable } from 'rxjs'
import { map } from 'rxjs/operators'


@Injectable({
  providedIn: 'root'
})
export class FireUpService {
  WellCollection: AngularFirestoreCollection<Well>
  items: Observable<Well[]>
  constructor(private afs: AngularFirestore) {
      // this.items = this.afs.collection('Well-Nodes').valueChanges();
      this.items = this.afs.collection('Well-Nodes').snapshotChanges().pipe(
        map(res => {
          return res.map(a => {
            const data = a.payload.doc.data() as Well;
            data.id = a.payload.doc.id;
            return data;
          });
        })
      )
   }

   getWells(){
     return this.items;
   }

   getWellById(wellID: string){
    return this.afs.collection('Well-Nodes').doc(wellID).snapshotChanges().pipe(
      map(res => {
        const data = res.payload.data() as Well;
        data.id = res.payload.id;
        return data;
      })
    );
   }

   getReadings(wellID: string){
     return this.afs.collection('Well-Nodes').doc(wellID).collection('Readings').snapshotChanges().pipe(
       map(res => {
        return res.map(a => {
          const data = a.payload.doc.data() as reading;
          data.id = a.payload.doc.id;
          return data;
        })
       })
     );

   }
}


