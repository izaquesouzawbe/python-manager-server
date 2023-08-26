export class Server {

  id: number;
  name: string;
  host: string;
  username: string;
  password: string;
  privateKey: string;

  constructor() {
    this.id = 0;
    this.name = '';
    this.host = '';
    this.username = '';
    this.password = '';
    this.privateKey = '';
  }
}
