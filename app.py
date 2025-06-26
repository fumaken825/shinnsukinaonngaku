import streamlit as st

def get_personality_from_music(music_preference):
    # ここに音楽の好みから性格を診断するロジックを実装します。
    # 例として、簡単なキーワードマッチングを行います。
    
    if "ロック" in music_preference:
        return "情熱的でエネルギッシュな性格です。新しいことに挑戦するのが好きで、リーダーシップを発揮するタイプでしょう。"
    elif "メタル" in music_preference:
        return "力強く芯のある性格です。困難に立ち向かう精神を持ち、仲間とともに熱い時間を楽しむ傾向があります。"
    elif "クラシック" in music_preference:
        return "落ち着きがあり、知的な性格です。物事を深く考える傾向があり、芸術や文化に興味があります。"
    elif "ジャズ" in music_preference:
        return "自由な発想を大切にする性格です。独創性があり、流れるようなライフスタイルを楽しみます。"
    elif "J-POP" in music_preference:
        return "親しみやすくバランスの取れた性格です。日常の小さな幸せを大切にし、人とのつながりを自然に楽しめるタイプです。"
    elif "K-POP" in music_preference:
        return "トレンドに敏感で華やかな性格です。自己プロデュースが上手で、SNSや流行に敏感な一面があります。"
    elif "アイドル" in music_preference:
        return "明るく社交的で、推し活を通して自分の気持ちを素直に表現できるタイプです。仲間とのつながりも大切にします。"
    elif "ヒップホップ" in music_preference:
        return "自己主張が強く、個性を大切にする性格です。逆境をバネにし、クリエイティブな才能を発揮することが得意です。"
    elif "R&B" in music_preference:
        return "情熱的でロマンチックな性格です。感情を大切にし、深い人間関係を築くのが得意です。"
    elif "EDM" in music_preference:
        return "活動的で冒険好きな性格です。パーティーの中心にいることが多く、刺激を求める傾向があります。"
    elif "テクノ" in music_preference:
        return "未来志向で論理的な性格です。システムや構造に興味を持ち、効率的に物事を進めます。"
    elif "アコースティック" in music_preference:
        return "穏やかで自然体な性格です。内省的で、人との深いつながりを大切にします。"
    elif "フォーク" in music_preference:
        return "素朴で温かみのある性格です。歴史や文化に興味があり、人との交流を楽しむタイプです。"
    elif "アニメソング" in music_preference:
        return "想像力豊かで感受性の強い性格です。現実と空想の世界を行き来しながら、自分の世界観を大切にします。"
    elif "ゲーム音楽" in music_preference:
        return "集中力が高く、戦略的な思考を持つ性格です。挑戦を楽しみながら成長を目指すタイプです。"
    elif "演歌" in music_preference:
        return "情に厚く、懐かしいものや人との絆を大切にする性格です。人情や人生の機微に敏感な一面があります。"
    elif "昭和歌謡" in music_preference:
        return "懐古的で感傷的な性格です。昔の良さを大切にし、伝統を重んじる一面があります。"
    elif "レゲエ" in music_preference:
        return "マイペースで自由を愛する性格です。細かいことにこだわらず、リラックスしたライフスタイルを好みます。"
    elif "スカ" in music_preference:
        return "陽気で楽観的な性格です。リズムを楽しみながら周囲を明るくするムードメーカーです。"
    elif "ボサノバ" in music_preference:
        return "おしゃれで感性が豊か、かつ心地よさを大切にする性格です。人とゆったり過ごす時間を楽しめるタイプです。"
    elif "ラテン" in music_preference:
        return "情熱的で陽気な性格です。社交的で人と楽しむ時間を大切にします。"
    else:
        return "あなたの音楽の好みからは、多様な可能性が感じられます。もしかしたら、まだ気づいていない新しい自分を発見できるかもしれませんね。"

st.title("音楽の好みで性格診断アプリ")

st.write("好きな音楽のジャンルを入力してください。あなたの音楽の好みから性格を診断します。")

music_input = st.text_area("あなたの好きな音楽について教えてください", "例：クラシック音楽")

if st.button("診断する"):
    if music_input:
        personality = get_personality_from_music(music_input)
        st.subheader("診断結果")
        st.write(personality)
    else:
        st.warning("何か入力してください。")
