/**
 * Updates a pseudotoken with card token information
 *
 * @param fastPaymentToken - Base64 encoded token data containing authentication
 * @param pseudotoken - The pseudotoken to update
 * @param cardToken - The card token to associate with the pseudotoken
 * @returns Promise that resolves when update is complete
 */
declare const updatePseudotoken: (fastPaymentToken: string, pseudotoken: string, cardToken: string) => Promise<void | undefined>;
export default updatePseudotoken;
