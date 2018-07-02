import pandas as pd

tourneys = {}
tourney_id = 0
surfaces = {}
surface_id = 0
tourney_levels = {}
tourney_level_id = 0
entries = {"": 0}
entry_id = 1
hands = {}
hand_id = 0
countries = {}
country_id = 0
rounds = {}
round_id = 0


def load_data(_paths):

    print("Loading data..")

    _x = []
    _y = []


    for _path in _paths:
        print("Loading and preparing \"" + str(_path) + "\"")
        _data_year = pd.read_csv(_path)
        _matches, _results = prepare_data(_data_year.get("tourney_name"), _data_year.get("surface"), _data_year.get("draw_size"),
                   _data_year.get("tourney_level"), _data_year.get("match_num"), _data_year.get("winner_id"),
                   _data_year.get("winner_seed"), _data_year.get("winner_entry"), _data_year.get("winner_hand"),
                   _data_year.get("winner_ht"), _data_year.get("winner_ioc"), _data_year.get("winner_age"),
                   _data_year.get("winner_rank"), _data_year.get("winner_rank_points"), _data_year.get("loser_id"),
                   _data_year.get("loser_seed"), _data_year.get("loser_entry"), _data_year.get("loser_hand"),
                   _data_year.get("loser_ht"), _data_year.get("loser_ioc"), _data_year.get("loser_age"),
                   _data_year.get("loser_rank"), _data_year.get("loser_rank_points"), _data_year.get("best_of"),
                   _data_year.get("round"), _data_year.get("minutes"), _data_year.get("w_ace"), _data_year.get("w_df"),
                   _data_year.get("w_svpt"), _data_year.get("w_1stIn"), _data_year.get("w_1stWon"),
                   _data_year.get("w_2ndWon"), _data_year.get("w_SvGms"), _data_year.get("w_bpSaved"),
                   _data_year.get("w_bpFaced"), _data_year.get("l_ace"), _data_year.get("l_df"),
                   _data_year.get("l_svpt"), _data_year.get("l_1stIn"), _data_year.get("l_1stWon"),
                   _data_year.get("l_2ndWon"), _data_year.get("l_SvGms"), _data_year.get("l_bpSaved"),
                   _data_year.get("l_bpFaced"))
        _x.extend(_matches)
        _y.extend(_results)

    print("Data loaded and prepared.")

    return _x, _y


def prepare_data(_tourney_names, _surfaces, _draw_sizes, _tourney_levels, _match_nums, _p1_ids, _p1_seeds, _p1_entries,
               _p1_hands, _p1_hts, _p1_iocs, _p1_ages, _p1_ranks, _p1_rank_points, _p2_ids, _p2_seeds, _p2_entries,
               _p2_hands, _p2_hts, _p2_iocs, _p2_ages, _p2_ranks, _p2_rank_points, _best_ofs, _rounds, _minutes,
               _p1_aces, _p1_dfs, _p1_svpts, _p1_1stIns, _p1_1stWons, _p1_2ndWons, _p1_SvGms, _p1_bpSaved, _p1_bpFaced,
               _p2_aces, _p2_dfs, _p2_svpts, _p2_1stIns, _p2_1stWons, _p2_2ndWons, _p2_SvGms, _p2_bpSaved, _p2_bpFaced):

    global tourneys, tourney_id, surfaces, surface_id, tourney_levels, tourney_level_id, entries, entry_id
    global hands, hand_id, countries, country_id, rounds, round_id

    _matches = []
    _results = []

    for i in range(0, len(_tourney_names)):
        _match_data = []

        if _tourney_levels[i] == "D":
            continue

        # tourney_name

        if _tourney_names[i] != _tourney_names[i]:
            continue
        if _tourney_names[i] not in tourneys:
            tourneys[_tourney_names[i]] = tourney_id
            tourney_id += 1
        _match_data.append(tourneys[_tourney_names[i]])

        # surface

        if _surfaces[i] != _surfaces[i]:
            continue
        if _surfaces[i] not in surfaces:
            surfaces[_surfaces[i]] = surface_id
            surface_id += 1
        _match_data.append(surfaces[_surfaces[i]])

        # draw_size

        if _draw_sizes[i] != _draw_sizes[i]:
            continue
        _match_data.append(_draw_sizes[i])

        # tourney_level

        if _tourney_levels[i] != _tourney_levels[i]:
            continue
        if _tourney_levels[i] not in tourney_levels:
            tourney_levels[_tourney_levels[i]] = tourney_level_id
            tourney_level_id += 1
        _match_data.append(tourney_levels[_tourney_levels[i]])

        # match_num

        if _match_nums[i] != _match_nums[i]:
            continue
        _match_data.append(_match_nums[i])

        # p1_id

        if _p1_ids[i] != _p1_ids[i]:
            continue
        _match_data.append(_p1_ids[i] - 100000)

        # p1_seed

        if _p1_seeds[i] != _p1_seeds[i]:
            _match_data.append(_draw_sizes[i]//2)
        else:
            _match_data.append(_p1_seeds[i])

        # p1_entry

        _entry = ""
        if _p1_entries[i] == _p1_entries[i] and _p1_entries[i] not in entries:
            _entry = _p1_entries[i]
            entries[_entry] = entry_id
            entry_id += 1
        _match_data.append(entries[_entry])

        # p1_hand

        if _p1_hands[i] != _p1_hands[i]:
            continue
        if _p1_hands[i] not in hands:
            hands[_p1_hands[i]] = hand_id
            hand_id += 1
        _match_data.append(hands[_p1_hands[i]])

        # p1_ht

        if _p1_hts[i] != _p1_hts[i]:
            continue
        _match_data.append(_p1_hts[i])

        # p1_ioc

        if _p1_iocs[i] != _p1_iocs[i]:
            continue
        if _p1_iocs[i] not in countries:
            countries[_p1_iocs[i]] = country_id
            country_id += 1
        _match_data.append(countries[_p1_iocs[i]])

        # p1_age

        if _p1_ages[i] != _p1_ages[i]:
            continue
        _match_data.append(_p1_ages[i])

        # p1_rank

        if _p1_ranks[i] != _p1_ranks[i]:
            continue
        _match_data.append(_p1_ranks[i])

        # p1_rank_points

        if _p1_rank_points[i] != _p1_rank_points[i]:
            continue
        _match_data.append(_p1_rank_points[i])

        # p2_id

        if _p2_ids[i] != _p2_ids[i]:
            continue
        _match_data.append(_p2_ids[i] - 100000)

        # p2_seed

        if _p2_seeds[i] != _p2_seeds[i]:
            _match_data.append(_draw_sizes[i] // 2)
        else:
            _match_data.append(_p2_seeds[i])

        # p2_entry

        _entry = ""
        if _p2_entries[i] == _p2_entries[i] and _p2_entries[i] not in entries:
            _entry = _p2_entries[i]
            entries[_entry] = entry_id
            entry_id += 1
        _match_data.append(entries[_entry])

        # p2_hand

        if _p2_hands[i] != _p2_hands[i]:
            continue
        if _p2_hands[i] not in hands:
            hands[_p2_hands[i]] = hand_id
            hand_id += 1
        _match_data.append(hands[_p2_hands[i]])

        # p2_ht

        if _p2_hts[i] != _p2_hts[i]:
            continue
        _match_data.append(_p2_hts[i])

        # p2_ioc

        if _p2_iocs[i] != _p2_iocs[i]:
            continue
        if _p2_iocs[i] not in countries:
            countries[_p2_iocs[i]] = country_id
            country_id += 1
        _match_data.append(countries[_p2_iocs[i]])

        # p2_age

        if _p2_ages[i] != _p2_ages[i]:
            continue
        _match_data.append(_p2_ages[i])

        # p2_rank

        if _p2_ranks[i] != _p2_ranks[i]:
            continue
        _match_data.append(_p2_ranks[i])

        # p2_rank_points

        if _p2_rank_points[i] != _p2_rank_points[i]:
            continue
        _match_data.append(_p2_rank_points[i])

        # best_of

        if _best_ofs[i] != _best_ofs[i]:
            _match_data.append(3)
        else:
            _match_data.append(_best_ofs[i])

        # round

        if _rounds[i] != _rounds[i]:
            continue
        if _rounds[i] not in rounds:
            rounds[_rounds[i]] = round_id
            round_id += 1
        _match_data.append(rounds[_rounds[i]])

        # minutes

        if _minutes[i] != _minutes[i]:
            continue
        _match_data.append(_minutes[i])

        # p1_ace

        if _p1_aces[i] != _p1_aces[i]:
            continue
        _match_data.append(_p1_aces[i])

        # p1_df

        if _p1_dfs[i] != _p1_dfs[i]:
            continue
        _match_data.append(_p1_dfs[i])

        # p1_svpt

        if _p1_svpts[i] != _p1_svpts[i]:
            continue
        _match_data.append(_p1_svpts[i])

        # p1_1stIn

        if _p1_1stIns[i] != _p1_1stIns[i]:
            continue
        _match_data.append(_p1_1stIns[i])

        # p1_1stWon

        if _p1_1stWons[i] != _p1_1stWons[i]:
            continue
        _match_data.append(_p1_1stWons[i])

        # p1_2ndWon

        if _p1_2ndWons[i] != _p1_2ndWons[i]:
            continue
        _match_data.append(_p1_2ndWons[i])

        # p1_SvGms

        if _p1_SvGms[i] != _p1_SvGms[i]:
            continue
        _match_data.append(_p1_SvGms[i])

        # p1_bpSaved

        if _p1_bpSaved[i] != _p1_bpSaved[i]:
            continue
        _match_data.append(_p1_bpSaved[i])

        # p1_bpFaced

        if _p1_bpFaced[i] != _p1_bpFaced[i]:
            continue
        _match_data.append(_p1_bpFaced[i])

        # p2_ace

        if _p2_aces[i] != _p2_aces[i]:
            continue
        _match_data.append(_p2_aces[i])

        # p2_df

        if _p2_dfs[i] != _p2_dfs[i]:
            continue
        _match_data.append(_p2_dfs[i])

        # p2_svpt

        if _p2_svpts[i] != _p2_svpts[i]:
            continue
        _match_data.append(_p2_svpts[i])

        # p2_1stIn

        if _p2_1stIns[i] != _p2_1stIns[i]:
            continue
        _match_data.append(_p2_1stIns[i])

        # p2_1stWon

        if _p2_1stWons[i] != _p2_1stWons[i]:
            continue
        _match_data.append(_p2_1stWons[i])

        # p2_2ndWon

        if _p2_2ndWons[i] != _p2_2ndWons[i]:
            continue
        _match_data.append(_p2_2ndWons[i])

        # p2_SvGms

        if _p2_SvGms[i] != _p2_SvGms[i]:
            continue
        _match_data.append(_p2_SvGms[i])

        # p2_bpSaved

        if _p2_bpSaved[i] != _p2_bpSaved[i]:
            continue
        _match_data.append(_p2_bpSaved[i])

        # p2_bpFaced

        if _p2_bpFaced[i] != _p2_bpFaced[i]:
            continue
        _match_data.append(_p2_bpFaced[i])

        _match_data2 = []
        _match_data2.extend(_match_data[:5])
        _match_data2.extend(_match_data[14:23])
        _match_data2.extend(_match_data[5:14])
        _match_data2.extend(_match_data[23:26])
        _match_data2.extend(_match_data[35:])
        _match_data2.extend(_match_data[26:35])

        _matches.append(_match_data)
        _matches.append(_match_data2)
        _results.append(0)
        _results.append(1)

    return _matches, _results


if __name__ == '__main__':
    paths = [
        "data/atp_matches_2000.csv",
        "data/atp_matches_2001.csv",
        "data/atp_matches_2002.csv",
        "data/atp_matches_2003.csv",
        "data/atp_matches_2004.csv",
        "data/atp_matches_2005.csv",
        "data/atp_matches_2006.csv",
        "data/atp_matches_2007.csv",
        "data/atp_matches_2008.csv",
        "data/atp_matches_2009.csv",
        "data/atp_matches_2010.csv",
        "data/atp_matches_2011.csv",
        "data/atp_matches_2012.csv",
        "data/atp_matches_2013.csv",
        "data/atp_matches_2014.csv",
        "data/atp_matches_2015.csv",
        "data/atp_matches_2016.csv",
        "data/atp_matches_2017.csv",
        "data/atp_matches_2018.csv"
    ]

    x, y = load_data(paths)
