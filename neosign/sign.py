import argparse
import binascii
from prompt_toolkit import prompt
from neocore.KeyPair import KeyPair
from neocore.Cryptography.Crypto import Crypto


def main():
    parser = argparse.ArgumentParser(description='A utility for signing messages.  Example usage: "like "neosign mymessage -n"')
    parser.add_argument('message', type=str, help='The message in hex string format to be signed')
    parser.add_argument('-n', '--nep2', action='store_true', help="Whether to use an NEP2 passhrase rather than a wallet")
    parser.add_argument('-w', '--wif', type=str, default=None, help='If using a wif pass in the wif')
    args = parser.parse_args()
    try:

        if args.nep2:

            nep2_key = prompt('[nep2 key]> ', is_password=True)
            nep2_passwd = prompt("[nep2 key password]> ", is_password=True)

            prikey = KeyPair.PrivateKeyFromNEP2(nep2_key, nep2_passwd)
            keypair = KeyPair(priv_key=prikey)
            address= addr_from_pubkey(keypair.PublicKey)
            print("Signing With Address %s " % address)
            signature = Crypto.Sign(args.message, prikey)

            pubkey = keypair.PublicKey.encode_point().decode('utf-8')
            signature = signature.hex()
            print("pubkey, sig: %s %s " % (pubkey, signature))

        elif args.wif:
            prikey = KeyPair.PrivateKeyFromWIF(args.wif)
            keypair = KeyPair(priv_key=prikey)
            address= addr_from_pubkey(keypair.PublicKey)
            print("Signing With Address %s " % address)
            signature = Crypto.Sign(args.message, prikey)

            pubkey = keypair.PublicKey.encode_point().decode('utf-8')
            signature = signature.hex()
            print("pubkey, sig: %s %s " % (pubkey, signature))

        else:
            raise Exception("Please Specify -n or -w")
    except Exception as e:
        print("Could not sign: %s " % e)


def addr_from_pubkey(pubkey):
    script = bytearray(b'\x21') + binascii.unhexlify(pubkey.encode_point(compressed=True)) + bytearray(b'\xac')
    return Crypto.ToAddress(Crypto.ToScriptHash(script, unhex=False))

if __name__=='__main__':
    main()