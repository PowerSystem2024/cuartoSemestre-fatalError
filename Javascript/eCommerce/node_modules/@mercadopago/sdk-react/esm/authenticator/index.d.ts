import type { ShowAuthenticatorOptions, PaymentRequestHandlerApplication, IAuthenticator } from './types';
/**
 * Creates a new authenticator instance for SuperToken authentication
 * This feature is disabled by deafult, to enable it, please contact the offical *Mercado Pago* support via developer's website: www.mercadopago.com/developers
 * @param amount - The amount to be processed on the payment request
 * @param payerEmail - The email of the payer
 * @returns Promise that resolves to an authenticator instance
 */
declare const createAuthenticator: (amount: string, payerEmail: string) => Promise<IAuthenticator>;
export default createAuthenticator;
export type { ShowAuthenticatorOptions, IAuthenticator, PaymentRequestHandlerApplication };
