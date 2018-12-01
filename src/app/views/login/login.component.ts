import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../../models/user'
import { AuthService } from '../../services/auth_service/auth.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: 'login.component.html'
})
export class LoginComponent { 
  // user:User;
  user= {
    email:'',
    password:''
  };
  constructor(private authService: AuthService,private router: Router){

  }
  signInWithEmail() {
    this.authService.signInRegular(this.user.email, this.user.password)
      .then((res) => {
        console.log(res);

        this.router.navigate(['dashboard']);
      })
      .catch((err) => console.log('error: ' + err));
  }
}
