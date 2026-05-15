const { createClient } = require('@supabase/supabase-js');
const SUPABASE_URL = "https://exooykvgjxckvcnxhiap.supabase.co";
const SUPABASE_KEY = "sb_publishable_i5paySUP8L7xAGsBENbBBg_UC3Eu_Fm";
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function test() {
    const credentials = [
        { email: 'admin@isctem.ac.mz', pass: 'role123' },
        { email: 'gestor@isctem.ac.mz', pass: 'role123' },
        { email: 'docente@isctem.ac.mz', pass: 'role123' },
        { email: 'admin@isctem.ac.mz', pass: 'admin123' }
    ];

    for (const cred of credentials) {
        const { data, error } = await supabase.auth.signInWithPassword({
            email: cred.email,
            password: cred.pass
        });
        if (error) {
            console.log(`FAILED: ${cred.email} with ${cred.pass} - ${error.message}`);
        } else {
            console.log(`SUCCESS: ${cred.email} with ${cred.pass}`);
            await supabase.auth.signOut();
        }
    }
}

test();
