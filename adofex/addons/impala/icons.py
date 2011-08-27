#!/usr/bin/env python

rules = [
('accept_translation', 'database_edit.png'),
('action', 'lightning.png'),
('action_go', 'progress.gif'),
('actionlog', 'time.png'),
('admin', 'award_star_gold_1.png'),
('added, add', 'add.png'),
('add_disabled', 'add_disabled.png'),
('allow_file', 'database_edit.png'),
('bell', 'bell.png'),
('book', 'book_open.png'),
('branch', 'arrow_branch.png'),

('bullet_delete', 'bullet_delete.png'),
('bullet_green', 'bullet_green.png'),
('bullet_lock', 'bullet_lock.png'),

('bug', 'bug.png'),
('clone', 'layers.png'),
('clock', 'clock.png'),
('cog', 'cog.png'),
('copy_source', 'next.png'),
('collection', 'basket.png'),
('comment', 'comment.png'),
('comment_user', 'user_comment.png'),
('component', 'brick.png'),
('bricks', 'bricks.png'),
('compress', 'compress.png'),
('connect', 'connect.png'),
('coordinators', 'user_suit.png'),
('deleted, delete', 'cross.png'),
('delete_circle', 'cancel.png'),
('downsource', 'package.png'),
('drink', 'drink.png'),
('changed, edit', 'pencil.png'),
('edit_file', 'page_white_edit.png'),
('email', 'email.png'),
('cache', 'lorry.png'),
('cache_empty', 'lorry_flatbed.png'),
('comment', 'comment.png'),
('feed', 'feed.png'),
('file_search', 'folder_explore.png'),
('filter', 'filter.png'),
('find', 'magnifier.png'),
('find_file', 'page_add.png'),
('flag_green', 'flag_green.png'),
('freeze', 'date_error.png'),
('get_file', 'page_white_get.png'),
('homepage', 'house.png'),
('help', 'help.png'),
('key', 'key.png'),
('like', 'thumb_up.png'),
('lock', 'lock.png'),
('lock_break', 'lock_break.png'),
('lock_none', 'lock_none.png'),
('logout', 'door_out.png'),
('maintainer', 'user_gray.png'),
('next', 'next.png'),
('error, notice', 'exclamation.png'),
('nudge', 'user_go.png'),
('language', 'comment.png'),
('link', 'world_link.png'),
('linkedin', 'linkedin.png'),
('location', 'world.png'),
('url_update', 'arrow_merge.png'),
('multifile', 'page_white_stack.png'),
('omega', 'text_letter_omega.png'),
('person_details', 'vcard.png'),
('project', 'package.png'),
('redo', 'arrow_redo.png'),
('reject', 'thumb_down.png'),
('previous', 'previous.png'),
('date, read', 'text_signature.png'),
('release', 'date.png'),
('release_date', 'date_go.png'),
('repository', 'drive_network.png'),
('resource', 'brick.png'),
('reviews', 'page_white_ruby.png'),
('ruby', 'ruby.png'),
('save', 'disk.png'),
('spellcheck', 'spellcheck.png'),
('override_save', 'disk.png'),
('save_all', 'disk_multiple.png'),
('search_translations', 'page_magnify.png'),
('send_file', 'page_white_put.png'),
('sitemap_color', 'sitemap_color.png'),
('smile', 'emoticon_smile.png'),
('source_code', 'database_gear.png'),
('star', 'star.png'),
('stats', 'chart_bar.png'),
('stringnum', 'bricks.png'),
('stats_edit', 'chart_bar_edit.png'),
('stop', 'delete.png'),
('status', 'contrast.png'),
('structure', 'sitemap.png'),
('submit', 'tick.png'),
('submitted, submit_file', 'page_white_put.png'),
('tag', 'tag_blue.png'),
('team', 'group.png'),
('team_join', 'group_add.png'),
('team_user_request', 'user_red.png'),
('team_request', 'group_gear.png'),
('text', 'page_white_text.png'),
('tick', 'tick.png'),
('tick_disabled', 'tick_disabled.png'),
('tick_circle', 'accept.png'),
('tip', 'lightbulb.png'),
('twitter', 'twitter.png'),
('user', 'user.png'),
('user_delete', 'user_delete.png'),
('waiting', 'progress.gif'),
('watch', 'eye.png'),
('watch_add', 'email_add.png'),
('watch_error', 'email_error.png'),
('watch_remove', 'email_delete.png'),
('undo', 'arrow_undo.png'),
('override_undo', 'arrow_undo.png'),
('view', 'page_magnify.png'),
('view_online', 'magnifier.png'),
]

rule = \
"%(selectors)s{background-image:url('../../images/icons/%(image)s'),-moz-linear-gradient(%(colors)s);\n" + \
"\tbackground-image:url('../../images/icons/%(image)s'),-webkit-linear-gradient(%(colors)s);\n" +\
"\tbackground-image:url('../../images/icons/%(image)s'),-o-linear-gradient(%(colors)s);}\n"
for (selectors, image) in rules:
    selectors = [s.strip() for s in selectors.split(",")]
    selectors_normal = ",".join([(".i16.%s.buttonized" % s) for s in selectors])
    selectors_hover = ",".join([(".i16.%s.buttonized:hover" % s) for s in selectors])

    print rule % {'selectors':selectors_normal, 'image': image, 'colors': "#efefef, #cfcfcf"},
    print rule % {'selectors':selectors_hover,  'image': image, 'colors': "#fafafa, #dadada"},
