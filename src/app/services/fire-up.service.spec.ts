import { TestBed } from '@angular/core/testing';

import { FireUpService } from './fire-up.service';

describe('FireUpService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FireUpService = TestBed.get(FireUpService);
    expect(service).toBeTruthy();
  });
});
