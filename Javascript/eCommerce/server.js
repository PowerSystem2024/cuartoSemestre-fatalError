import express from 'express';
import cors from 'cors';
import { MercadoPagoConfig, Preference } from 'mercadopago';

const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(cors());

// SDK de Mercado Pago
const client = new MercadoPagoConfig({ 
  accessToken: 'APP_USR-5138807399143433-090316-5983805289762bc4e5e2232b0522211b-516647193' 
});

// Ping de prueba
app.get('/ping', (req, res) => { 
  res.send('pong');
});

// Crear preferencia
app.post('/create_preference', async (req, res) => {
  try {
    const items = req.body.items || [
      {
        title: 'Mi producto',
        quantity: 1,
        unit_price: 2000
      }
    ];

    const preference = new Preference(client);
    const result = await preference.create({
      body: {
        items
      }
    });

    res.status(200).json({ 
      preference_id: result.id,
      init_point: result.init_point
    });

  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});

