import express from "express";
import cors from "cors";
import { MercadoPagoConfig, Preference } from "mercadopago";

const app = express();
app.use(express.json());
app.use(cors());

// Initialize MercadoPago client with access token
const client = new MercadoPagoConfig({
  accessToken: 'APP_USR-5607452383900402-091518-0db59a9c5d53ab08b2af616063f899b5-2695069118'
});

app.get('/ping', (req, res) => {
  res.json({ message: 'pong' });
});

app.post('/create_preference', async (req, res) => {
  try {
    const preference = {
      items: [
        {
          title: 'Mi producto',
          quantity: 1,
          unit_price: 2000
        }
      ]
    };

    // Create preference using the client
    const mpPreference = new Preference(client);
    const response = await mpPreference.create({ body: preference });

    res.status(200).json({
      preference_id: response.id,
      preference_url: response.init_point
    });
  } catch (error) {
    console.error('Error creating preference:', error);
    res.status(500).json({ error: 'Error creating preference' });
  }
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});