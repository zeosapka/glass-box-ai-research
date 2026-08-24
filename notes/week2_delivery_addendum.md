# Week 2 Teslim Addendum — Son Kontrol ve Dokümantasyon Tamamlama

Bu dosya, Week 2 (E06–E12) tesliminden hemen önce yapılan son dokümantasyon kontrolünde tespit edilen küçük eksikleri kapatmak için eklenmiştir. Ana deney sonuçlarını değiştirmez; deneylerin yorumunu daha açık, denetlenebilir ve teslim edilebilir hale getirir.

> **Kapsam:** E06–E12. Bu addendum deney sonuçlarının yerine geçmez; `experiments/week2_experiment_records.md`, ilgili notebooklar, grafikler ve Week 2 raporu ana kaynak olarak kalır.

---

## 1. E06 — Başarım kriteri açıklaştırıldı

E06 için teslim kriteri iki parçalıdır:

| Kriter | Eşik | Gerçekleşen |
|---|---:|---:|
| Seed'lerin en az üçünde aday etki | `≤ -5.0 pp` | **5/5** |
| Her seed'de aday/control etki oranı | `> 3×` | **5/5** |

### Seed bazlı kontrol

| Seed | Aday Etki (pp) | Random Etki (pp) | Aday/Random |
|---:|---:|---:|---:|
| 42 | -14.8980 | +0.1020 | **146.00×** |
| 0 | -77.8571 | -2.5510 | **30.52×** |
| 7 | -25.2041 | -0.3061 | **82.33×** |
| 123 | -10.6122 | +0.3061 | **34.67×** |
| 2024 | -9.7959 | +0.7143 | **13.71×** |

**Sonuç:** E06 başarı kriteri **PASS**. Beş seed'in tamamı hem `≤ -5 pp` etki kriterini hem de `>3×` aday/random ayrım kriterini karşılamaktadır.

**Yorum sınırı:** Bu sonuç çoklu-seed tekrarlanabilirlik ve güçlü etki büyüklüğü için kanıttır; tek başına formal istatistiksel anlamlılık veya mekanizmanın eksiksiz çözüldüğü iddiası değildir.

---

## 2. E07 — Discovery/Holdout doğrulamasının istatistiksel ek kontrolü

E07'nin mevcut deney kaydında Discovery ve Holdout karşılaştırması zaten bulunmaktadır:

| Ölçüm | Discovery | Holdout |
|---|---:|---:|
| Aday ortalama L1 | **2.127904** | **1.962849** |
| Random control ortalama L1 | **0.123722** | **0.124925** |
| Aday/control oranı | **17.20×** | **15.71×** |
| Aday ortalamasını geçen control | **0/20** | **0/20** |

Bu addendum ile birlikte E07'nin doğrulama kaydına dağılım-tabanlı kontrolün ayrıca raporlanması hedeflenmiştir.

### Önemli metodolojik not

E07'nin mevcut kayıtlarında 20 random control değerinin tamamı tutulmaktadır; ancak standart kayıt alanında formal `z` / percentile sonucu daha önce yazılmamıştır. Bu nedenle burada **yeni bir deney sonucu uydurulmamıştır**. Formal z-score hesabının kullanılacağı formül ve gerekli kontrol dağılımı açıkça tanımlanmıştır:

`z = (candidate_mean - control_mean) / std(control_values)`

`percentile = percentile_rank(candidate_mean, control_values)`

Bu iki değer, notebook'taki aynı 20 control gözlemi üzerinden hesaplandığında kayıt altına alınmalıdır. Hesaplama yeniden çalıştırılmadan sabit bir sayı deney sonucu olarak sunulmaz.

**Mevcut güvenilir doğrulama:** Holdout'ta `0/20` control boyutunun aday ortalamasını geçmesi ve aday/control oranının `15.71×` olmasıdır.

---

## 3. E12 — Local LLM kullanım amacı

E12'de Ollama ile lokal `llama3.2:1b` modeli çalıştırılmış, üç prompt test edilmiş ve modelin lokal olarak yürütüldüğü doğrulanmıştır. Bu deneyin Glass Box araştırmasındaki rolü aşağıdaki şekilde tanımlanır:

> **Glass Box araştırmasında Ollama, model içi mekanizma kanıtı üretmek için değil, araştırma iş akışında kullanılan açıklama/özetleme/hipotez üretme yardımcısının lokal ve tekrarlanabilir bir örneğini değerlendirmek için kullanılabilir.** Lokal çalıştırma sayesinde prompt, model ve çıktıların dış bir API'ye gönderilmeden kontrollü bir ortamda denenmesi mümkün olur. Ancak lokal LLM çıktısı tek başına nöron, feature veya devre düzeyinde mekanistik kanıt sayılmaz; mekanistik iddialar yine activation, intervention, causal effect ve kontrol deneyleriyle doğrulanmalıdır.

### E12 teslim özeti

| Alan | Değer |
|---|---|
| Runtime | **Ollama / local execution** |
| Model | **Llama 3.2 1B (`llama3.2:1b`)** |
| Prompt sayısı | **3** |
| Local execution | **True** |
| Mechanistic evidence | **False** |
| Araştırmadaki rol | Yardımcı açıklama/hipotez aracı; mekanistik kanıt değil |

---

## 4. E12 — Kurulum ve çalıştırma kaydı

Teslim açısından minimum yeniden üretim akışı:

1. Linux ortamında Ollama kurulumu.
2. Ollama servisinin çalıştırılması.
3. `llama3.2:1b` modelinin indirilmesi.
4. Notebook'un Ollama API'ye bağlanması.
5. Üç test promptunun çalıştırılması.
6. Lokal yürütmenin ve model adının çıktı içinde doğrulanması.
7. Sonuçların `notes/experiment_log_week2.md` ve E12 deney kaydında tutulması.

Bu addendum, kurulum adımlarının teslimde görünür olması için indeks görevi görür. Ham terminal çıktıları notebook çıktılarında korunur.

---

## 5. Commit / reproducibility durumu

Deney kayıtlarında `Commit hash` alanı bulunmaktadır. Ancak **deneylerin çalıştırıldığı kesin commit ile yalnızca dosyanın mevcut olduğu sonraki repository snapshot'ını birbirine karıştırmamak gerekir.**

Mevcut repository'de Week 2 notebooklarının güncel dosya snapshot'ı `4b3d111741931f8825eb5525a49d0690174d00eb` commit/ref üzerinde görülebilmektedir. Bu değer **dosya snapshot referansıdır**; deneyin çalıştırıldığı commit olarak ancak notebook çıktılarının bu snapshot'ta üretildiği doğrulanırsa kullanılmalıdır.

Bu nedenle:

| Alan | Durum |
|---|---|
| Notebookların erişilebilir commit/ref'i | `4b3d111741931f8825eb5525a49d0690174d00eb` |
| E06–E12 deneylerinin kesin execution commit'i | **Ana kayıtta ayrı belirtilmemiş** |
| Önerilen teslim uygulaması | Notebook çıktıları bu snapshot'ta üretildiyse bu hash'i execution snapshot olarak belirtmek |

**Not:** Burada doğrulanmamış bir commit hash'i deney execution hash'i olarak uydurulmamıştır.

---

## 6. Week 2 teslim kontrol tablosu

| Teslim öğesi | Durum | Kaynak |
|---|:---:|---|
| E06 notebook + kayıt | ✅ | `07_multiseed_circuit_replication.ipynb` |
| E07 notebook + kayıt | ✅ | `08_matched_transformer_experiment.ipynb` |
| E08 notebook + kayıt | ✅ | `09_graded_transformer_intervention.ipynb` |
| E09 notebook + kayıt | ✅ | `10_statistical_control_test.ipynb` |
| E10 notebook + kayıt | ✅ | `11_group_intervention.ipynb` |
| E11 notebook + kayıt | ✅ | `12_synthetic_true_vs_spurious_feature.ipynb` |
| E12 notebook + kayıt | ✅ | `13_local_llm_ollama.ipynb` |
| E06 multi-seed başarı kriteri | ✅ | 5/5 seed, `≤ -5 pp`; 5/5 seed, `>3×` |
| E07 Discovery/Holdout | ✅ | 0/20 control exceeded candidate; Holdout `15.71×` |
| E07 formal z/percentile | ⚠️ | Hesap formülü tanımlı; sayı yeniden hesaplanmadan sabitlenmedi |
| E12 kullanım amacı açıklaması | ✅ | Bu addendum'da açıklandı |
| E12 kurulum akışı | ✅ | Bu addendum + notebook |
| Grafikler | ✅ | `figures/figure_index.md` ve `figures/week2/` |
| Literatür | ✅ | `notes/literature_table.md` |
| Week 2 raporu | ✅ | `report/week2_report.md` |
| Week 2 sunumu | ✅ | `report/week2_presentation.md` |
| Glass Box computational map | ✅ | `report/glass_box_map.md` |

---

## 7. Final teslim notu

Bu addendum'un amacı yeni bir deney eklemek değil, mevcut Week 2 sonuçlarının **başarım kriteri, doğrulama, kullanım amacı ve yeniden üretilebilirlik** tarafını teslim öncesinde daha görünür hale getirmektir.

Özellikle:

- E06'nın `>3×` kontrol eşiği artık açıkça kayıtlıdır.
- E07'nin Discovery/Holdout sonucu tablo halinde görünürdür; formal z/percentile sayılarını veri yeniden hesaplanmadan uydurmamak için yöntem açıkça belirtilmiştir.
- E12'nin Glass Box iş akışındaki rolü ve mekanistik kanıt olmadığı açıkça yazılmıştır.
- Kurulum/reproduction akışı tek yerde özetlenmiştir.
- Commit konusunda dosya snapshot'ı ile execution commit'i birbirinden ayrılmıştır.

**Bu dosya, Week 2 tesliminin son kalite kontrol eki olarak kullanılabilir.**
